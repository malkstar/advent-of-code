# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals


with open('input.txt', 'r') as input_file:
    input_text_lines = input_file.readlines()

    results = [0,]
    current_frequency = 0

    def until_result_repeated(text_lines):
        global current_frequency
        found_result = False
        for line in text_lines:
            new_value = current_frequency + int(line)
            if new_value in results:
                print('First repeated: {}'.format(new_value))
                found_result = True
                break
            else:
                current_frequency = new_value
                results.append(current_frequency)

        if not found_result:
            until_result_repeated(text_lines)

    until_result_repeated(input_text_lines)
