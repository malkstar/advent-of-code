#!/usr/bin/python


def calculate_present_ribbon_length(input_dimensions):
    input_dimensions = sorted(input_dimensions)
    return (int(input_dimensions[0]) * 2) + (int(input_dimensions[1]) * 2)


def calculate_present_bow_length(l, w, h):
    return l * w * h

TOTAL_RIBBON_LENGTH = 0

with open('input.txt', 'r') as input_file:
    for line in input_file:
        int_dimensions = [int(measurement) for measurement in line.split('x')]
        TOTAL_RIBBON_LENGTH += calculate_present_ribbon_length(int_dimensions)
        TOTAL_RIBBON_LENGTH += calculate_present_bow_length(*int_dimensions)
    print 'ANSWER: {}'.format(TOTAL_RIBBON_LENGTH)
