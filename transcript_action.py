#!/usr/bin/env python
# coding: utf-8

import sys
import subprocess

from transcript import print_timecodes

if __name__ == '__main__':
    input_file = sys.argv[1]

    output_file = input_file \
        .replace('docs/', 'transcripts/') \
        .replace('.docx', '.txt')

    print(f'processing {input_file} -> {output_file}')

    print_timecodes(input_file, output_file)