#!/usr/bin/python


def has_pair_of_pairs(string):
    char_pairs = []
    for i, char in enumerate(string):
        char_pairs.append(string[i:i+2])
    for i, pair in enumerate(char_pairs):
        char_pairs.remove(pair)
        if pair in char_pairs and char_pairs.index(pair) - i > 1:
            return True
    return False


def has_repeating_letter(string):
    character_index_dict = {}
    for i, char in enumerate(string):
        if char in character_index_dict:
            if i - character_index_dict[char] == 2:
                return True
            else:
                character_index_dict[char] = i
        else:
            character_index_dict[char] = i
    return False


def is_nice(string):
    return has_pair_of_pairs(string) and has_repeating_letter(string)

NICE_STRINGS = 0

with open('input.txt', 'r') as input_file:
    for line in input_file:
        if is_nice(line.strip()):
            NICE_STRINGS += 1
    print(NICE_STRINGS)
