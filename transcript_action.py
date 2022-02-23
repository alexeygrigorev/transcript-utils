#!/usr/bin/env python
# coding: utf-8

import sys

from transcript import print_timecodes

def main(input_file):
    if not input_file.endswith('.docx'):
        print('not a docx file')
        return 

    output_file = input_file \
        .replace('docs/', 'transcripts/') \
        .replace('.docx', '.txt')

    print(f'processing {input_file} -> {output_file}')

    print_timecodes(input_file, output_file)


if __name__ == '__main__':
    input_file = sys.argv[1]
    main(input_file)
