# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals

with open('input.txt', 'r') as input_file:
    input_text = input_file.readlines()

    double_count = 0
    triple_count = 0

    for line in input_text:
        line_char_count = {}
        for char in line.strip():
            if char not in line_char_count:
                line_length = len(line)
                line_length_minus_char = len(line.replace(char, ''))
                line_char_count[char] = line_length - line_length_minus_char
        if 2 in line_char_count.values():
            double_count += 1
        if 3 in line_char_count.values():
            triple_count += 1

    print('Checksum: {} * {} = {}'.format(double_count, triple_count, double_count * triple_count))
