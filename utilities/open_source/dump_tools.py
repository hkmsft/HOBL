# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

##
# Dump tools
##

import argparse
import os
import json
import ast

scenario_docs = {}

def extract_docstrings(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        tree = ast.parse(file.read())

    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.Module)):
            if hasattr(node, "name"):
                docstring = ast.get_docstring(node)
                if docstring:
                    return docstring
    return None


def main(print_json=True, short=True):
    tools_dirs = [os.path.join(os.getcwd(), 'tools')]

    if print_json:
        arg_parser = argparse.ArgumentParser()
        arg_parser.add_argument('-hobl_external', '-he', default='')
        args = arg_parser.parse_args()
        hobl_ext_paths = args.hobl_external.split()

        [tools_dirs.append(os.path.join(ext, 'tools')) for ext in hobl_ext_paths]

    tools_seen = set()

    for tools_dir in tools_dirs:
        if not os.path.exists(tools_dir):
            continue

        for filename in os.listdir(tools_dir):
            if filename.endswith('.py') and filename != '__init__.py':
                if filename in tools_seen:
                    continue
                tools_seen.add(filename)

                # remove '.py' extension
                module_name = filename[:-3]

                module_path = os.path.join(tools_dir, filename)

                docstring = extract_docstrings(module_path)

                if short and docstring is not None:
                    # get first paragraph only
                    docstring = docstring.split('\n')[0]

                scenario_docs[module_name] = docstring

    if print_json:
        print(json.dumps(scenario_docs))


if __name__ == '__main__':
    main()
