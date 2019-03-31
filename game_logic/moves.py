import numpy as np
from random import randint


def insert_new_cell(field):
    zero_cells = np.where(field == 0)
    len_zeros = len(zero_cells[1])
    cell_to_fill = randint(0, len_zeros - 1)
    if randint(1, 10) == 10:
        valueToIns = 4
    else:
        valueToIns = 2
    field[zero_cells[0][cell_to_fill]][zero_cells[1][cell_to_fill]] = valueToIns
    return field


def get_initial_field(n):
    field = np.zeros(shape=(n, n))
    for i in range(2):
        field = insert_new_cell(field)
    return field


def move_row(r):
    return r


def move_field(field, move):
    new_points = 0
    if move == 'up':
        for i in range(len(field[1])):
            print(1)
    elif move == 'down':
        for i in range(len(field[1])):
            print(1)
    elif move == 'right':
        for i in range(len(field[1])):
            print(1)
    elif move == 'left':
        for i in range(len(field[1])):
            print(1)
    return field, new_points


def field_stucked(field):
    for mv in ['up', 'down', 'right', 'left']:
        fcopy = field.copy()
        if not np.array_equal(field, move_field(fcopy, mv)):
            return False
    return True
