#!/usr/bin/env python
# coding: utf-8

import sys
import subprocess

from transcript import print_timecodes


if __name__ == '__main__':
    sha = sys.argv[1]
    command = ['git', 'diff', '--name-only', sha, f'{sha}^1']

    changed_files = subprocess.check_output(command).decode()
    input_files = changed_files.split()

    for input_file in input_files:
        output_file = input_file \
            .replace('docs/', 'transcripts/') \
            .replace('.docx', '.txt')

        print(f'processing {input_file} -> {output_file}')

        print_timecodes(input_file, output_file)