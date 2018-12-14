# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals

with open('input.txt', 'r') as input_file:
    input_text = input_file.readlines()

    differences = []
    for line in input_text:
        ints = map(int, line.strip().split('\t'))
        smallest = min(ints)
        largest = max(ints)
        differences.append(largest-smallest)
    print(sum(differences))
