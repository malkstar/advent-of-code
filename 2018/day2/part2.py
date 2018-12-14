# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals

import string


with open('input.txt', 'r') as input_file:
    input_text = input_file.readlines()

    box_ids_replaced = set([])
    for line in input_text:
        line = line.strip()
        line_length = len(line)
        for letter in string.ascii_lowercase:
            set_length = len(box_ids_replaced)
            removed_letter = line.replace(letter, '', 1)
            print(removed_letter)
            box_ids_replaced.add(removed_letter)
            if set_length == len(box_ids_replaced) and len(removed_letter) < line_length:
                print('{} happened twice!'.format(removed_letter))
