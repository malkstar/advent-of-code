# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals

with open('input.txt', 'r') as input_file:
    input_text = input_file.read().strip()

    repeated_numbers = []

    for index, character in enumerate(input_text):
        try:
            if character == input_text[index+1]:
                repeated_numbers.append(int(character))
        except IndexError:
            # at the end of the file, check this one against the first character
            if character == input_text[0]:
                repeated_numbers.append(int(character))
    print(sum(repeated_numbers))
