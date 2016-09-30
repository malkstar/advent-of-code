#!/usr/bin/python


def move_west():
    global CURRENT_X
    CURRENT_X -= 1
    log_current_location()


def move_east():
    global CURRENT_X
    CURRENT_X += 1
    log_current_location()


def move_north():
    global CURRENT_Y
    CURRENT_Y += 1
    log_current_location()


def move_south():
    global CURRENT_Y
    CURRENT_Y -= 1
    log_current_location()


def log_current_location():
    global CURRENT_X
    global CURRENT_Y
    global VISITED_COORDS
    VISITED_COORDS.append('{},{}'.format(CURRENT_X, CURRENT_Y))


CURRENT_X = 0
CURRENT_Y = 0
VISITED_COORDS = ['0,0']

function_mapping = {'>': move_east, '<': move_west, '^': move_north, 'v': move_south}

with open('input.txt', 'r') as input_file:
    input_text = input_file.read()
    for char in input_text.strip():
        function_mapping[char]()
    print('ANSWER: {}'.format(len(set(VISITED_COORDS))))
