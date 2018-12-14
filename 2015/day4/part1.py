#!/usr/bin/python
import hashlib

with open('input.txt', 'r') as input_file:
    input_text = input_file.read().strip()
    m = hashlib.md5(input_text)
    appended_number = 0
    while m.hexdigest()[0:5] != '00000':
        m = hashlib.md5(input_text)
        m.update(str(appended_number))
        appended_number += 1
    print('ANSWER: {}'.format(appended_number - 1))
