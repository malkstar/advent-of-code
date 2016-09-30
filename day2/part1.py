#!/usr/bin/python


def calculate_sq_ft_for_present(l, w, h):
    l_w = l * w
    w_h = w * h
    h_l = h * l
    surface_area = (2*l_w) + (2*w_h) + (2*h_l)
    slack = min(l_w, w_h, h_l)
    return surface_area + slack

TOTAL_SQ_FT = 0

with open('input.txt', 'r') as input_file:
    for line in input_file:
        int_dimensions = [int(measurement) for measurement in line.split('x')]
        TOTAL_SQ_FT += calculate_sq_ft_for_present(*int_dimensions)
    print 'ANSWER: {}'.format(TOTAL_SQ_FT)
