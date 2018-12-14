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


with open('input.txt', 'r') as input_file:
    input_text = input_file.read()

    x = 0
    y = 0
    
    current_direction = North
    
    for text in input_text.split(', '):
        turn = text[0:1]
        current_direction = NEW_DIRECTIONS[current_direction][turn]
        movement = int(text[1:])
        x, y = MOVE_COORDINATES[current_direction](x, y, movement)
    print('ANSWER: {}'.format(abs(x) + abs(y)))
