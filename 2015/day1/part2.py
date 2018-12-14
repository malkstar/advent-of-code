#!/usr/bin/python


def increment_floor():
    global FLOOR
    FLOOR += 1


def decrement_floor():
    global FLOOR
    FLOOR -= 1

FLOOR = 0

function_map = {'(': increment_floor, ')': decrement_floor}

with open('input.txt', 'r') as input_file:
    input_text = input_file.read()

    for idx, char in enumerate(input_text.strip()):
        function_map[char]()
        if FLOOR == -1:
            print('ANSWER: {}'.format(idx + 1))
            break
