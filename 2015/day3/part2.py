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


def log_current_location(robot=False):
    if robot:
        global ROBOT_X
        global ROBOT_Y
        x = ROBOT_X
        y = ROBOT_Y
    else:
        global CURRENT_X
        global CURRENT_Y
        x = CURRENT_X
        y = CURRENT_Y
    global VISITED_COORDS
    VISITED_COORDS.append('{},{}'.format(x, y))


def move_robot_west():
    global ROBOT_X
    ROBOT_X -= 1
    log_current_location(True)


def move_robot_east():
    global ROBOT_X
    ROBOT_X += 1
    log_current_location(True)


def move_robot_north():
    global ROBOT_Y
    ROBOT_Y += 1
    log_current_location(True)


def move_robot_south():
    global ROBOT_Y
    ROBOT_Y -= 1
    log_current_location(True)


SANTA = True
CURRENT_X = 0
ROBOT_X = 0
CURRENT_Y = 0
ROBOT_Y = 0
VISITED_COORDS = ['0,0']

function_mapping = {'>': move_east, '<': move_west, '^': move_north, 'v': move_south}
robot_function_mapping = {
    '>': move_robot_east,
    '<': move_robot_west,
    '^': move_robot_north,
    'v': move_robot_south
}

with open('input.txt', 'r') as input_file:
    input_text = input_file.read()
    for char in input_text.strip():
        if SANTA:
            function_mapping[char]()
            SANTA = False
        else:
            robot_function_mapping[char]()
            SANTA = True
    print('ANSWER: {}'.format(len(set(VISITED_COORDS))))
