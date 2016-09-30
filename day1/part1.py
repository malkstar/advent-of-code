#!/usr/bin/python


def up_floor():
    global FLOOR
    FLOOR += 1


def down_floor():
    global FLOOR
    FLOOR -= 1

FLOOR = 0

function_map = {'(': up_floor, ')': down_floor}

with open('input.txt', 'r') as input_file:
    input_text = input_file.read()

    for char in input_text.strip():
        function_map[char]()

    print('ANSWER: {}'.format(FLOOR))
