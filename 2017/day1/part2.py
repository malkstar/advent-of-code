# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals

with open('input.txt', 'r') as input_file:
    input_text = input_file.read().strip()
    list_length = len(input_text)
    half_length = list_length / 2
    repeated_numbers = []

    for index, character in enumerate(input_text):
        try:
            if character == input_text[int(index+half_length)]:
                repeated_numbers.append(int(character))
        except IndexError:
            if character == input_text[int(index+half_length-list_length)]:
                repeated_numbers.append(int(character))
    print(sum(repeated_numbers))
