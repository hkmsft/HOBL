# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import sys
import argparse
import glob
import os
import csv
import collections
import pandas as pd

arg_parser = argparse.ArgumentParser(description = "Summarizes SystemDeck results into a list of key-vals.")
arg_parser.add_argument('-input', '-i', help='Path to sd summary .csv file.')
arg_parser.add_argument('-output', '-o', help='Path of output .csv file.')
args = arg_parser.parse_args()

df = pd.read_csv(args.input, sep=',', header=0, engine="python")
df = df.filter(regex=r'(?<=CORE\d\s)(Power|Freq\sEff)|((?<=OFF\s)Residency)|(?:Whisper\sMode)|(?:CstateBoost)|(?:GFX\sFreq)|(?:Refresh)|(?:DCE)|(?:IO\sReadsWrites)', axis=1)
s_mean = df.mean()
# grouped = s_mean.groupby(s_mean.index.str.extract(r'(?:CPU\d )?(?:.*CORE\d )?(.*)', expand=False)).mean()
# print(grouped)
s_mean = s_mean.add_prefix("SD ")
print (s_mean)
s_mean.to_csv(args.output, sep=',', float_format='%0.3f', header=False)
