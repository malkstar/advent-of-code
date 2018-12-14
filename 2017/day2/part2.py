# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals

with open('input.txt', 'r') as input_file:
    input_text = input_file.readlines()

    differences = []
    for line in input_text:
        ints = map(int, line.strip().split('\t'))
        found = False
        for number in ints:
            for number2 in ints:
                if number != number2 and number % number2 == 0:
                    differences.append(number / number2)
                    found = True
                    break
            if found:
                break
    print(sum(differences))
