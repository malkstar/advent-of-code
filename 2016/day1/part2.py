#!/usr/bin/python

North = 'North'
South = 'South'
East = 'East'
West = 'West'

NEW_DIRECTIONS = {
    North: {
        'L': West,
        'R': East
    },
    South: {
        'L': East,
        'R': West
    },
    East: {
        'L': North,
        'R': South
    },
    West: {
        'L': South,
        'R': North
    },
}

MOVE_COORDINATES = {
    North: lambda co_x, co_y, move: (co_x, co_y+move),
    South: lambda co_x, co_y, move: (co_x, co_y-move),
    East: lambda co_x, co_y, move: (co_x+move, co_y),
    West: lambda co_x, co_y, move: (co_x-move, co_y),
}

VISITED_COORDS = ['0, 0']


def traveled_coordinates(x, y, new_x, new_y):
    x_difference = abs(new_x - x)
    for x_coord in range(x_difference):
        if new_x - x > 0:
            traveled_coord = '{}, {}'.format(x + x_coord + 1, y)
        else:
            traveled_coord = '{}, {}'.format(x - x_coord - 1, y)
        if traveled_coord in VISITED_COORDS:
            print('ANSWER: {}'.format(sum([abs(int(coord)) for coord in traveled_coord.split(', ')])))
            return True
        else:
            VISITED_COORDS.append(traveled_coord)
    y_difference = abs(new_y - y)
    for y_coord in range(y_difference):
        if new_y - y > 0:
            traveled_coord = '{}, {}'.format(x, y + y_coord + 1)
        else:
            traveled_coord = '{}, {}'.format(x, y - y_coord - 1)
        if traveled_coord in VISITED_COORDS:
            print('ANSWER: {}'.format(sum([abs(int(coord)) for coord in traveled_coord.split(', ')])))
            return True
        else:
            VISITED_COORDS.append(traveled_coord)

with open('input.txt', 'r') as input_file:
    input_text = input_file.read()

    x = 0
    y = 0
    
    current_direction = North
    
    for text in input_text.split(', '):
        turn = text[0:1]
        current_direction = NEW_DIRECTIONS[current_direction][turn]
        movement = int(text[1:])
        new_x, new_y = MOVE_COORDINATES[current_direction](x, y, movement)
        if traveled_coordinates(x, y, new_x, new_y):
            break
        x = new_x
        y = new_y
