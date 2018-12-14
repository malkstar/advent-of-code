#!/usr/bin/python


def has_double_letters(string):
    last_char = ''
    for char in string:
        if char == last_char:
            return True
        last_char = char
    return False


def has_three_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    used_vowels = 0
    for char in string:
        if char in vowels:
            used_vowels += 1
            if used_vowels > 2:
                return True
    return False


def has_consecutive_letters(string):
    bad_strings = ['ab', 'cd', 'pq', 'xy']
    for bad_string in bad_strings:
        if bad_string in string:
            return True
    return False


def is_nice(string):
    return has_double_letters(string) and has_three_vowels(string) and not has_consecutive_letters(string)

NICE_STRINGS = 0

with open('input.txt', 'r') as input_file:
    for line in input_file:
        if is_nice(line.strip()):
            NICE_STRINGS += 1
    print(NICE_STRINGS)
