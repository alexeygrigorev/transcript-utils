#!/usr/bin/env python
# coding: utf-8

import sys

from transcript import process_trascript

def main(input_file):
    if not input_file.endswith('.docx'):
        print('not a docx file')
        return 

    output_file_timecodes = input_file \
        .replace('docs/', 'timecodes/') \
        .replace('.docx', '.txt')

    output_file_transcript = input_file \
        .replace('docs/', 'transcripts/') \
        .replace('.docx', '.yaml')

    print(f'processing {input_file}')
    process_trascript(
        input_file,
        output_file_timecodes,
        output_file_transcript
    )


if __name__ == '__main__':
    input_file = sys.argv[1]
    main(input_file)
