# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import argparse

args = None

class Arguments(object):
    def __init__(self, args_to_parse = None):
        # Command line arguments
        global args
        arg_parser = argparse.ArgumentParser(description = "HOBL test framework.")
        arg_parser.add_argument('-execute', '-e', help='Execute another Python script.')
        arg_parser.add_argument('-dump', '-d', help='Dump the default parameters.')
        arg_parser.add_argument('-dump_verbose', '-dv', help='Dump the default parameters verbosely.')
        arg_parser.add_argument('-profile', '-p', help='File that specifies test parameters.')
        arg_parser.add_argument('-scenarios', '-s', help='Test scenarios to run.  For multiple scenarios, separate with space and surround with quotes.')
        arg_parser.add_argument('-attempts', '-a', help='How many times to re-attempt a scenario that fails')
        arg_parser.add_argument('-kill', '-k', help='kill/cleanup specified scenario')
        arg_parser.add_argument('overrides', nargs=argparse.REMAINDER, help='Specify test parameter overrides in the format: <scenario>:<key>=<val>')
        if args_to_parse:
            # args_to_parse should be a list
            args = arg_parser.parse_args(args_to_parse)
        else:
            args = arg_parser.parse_args()
