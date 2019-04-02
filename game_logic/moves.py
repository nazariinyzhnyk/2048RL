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


def move_row(arr):
    row_points = 0
    arr = arr[arr != 0]
    for i in range(len(arr) - 1, 0, -1):
        if arr[i] == arr[i - 1]:
            arr[i] *= 2
            row_points += arr[i]
            arr[i - 1] = 0
    arr = arr[arr != 0]
    arr = np.append(np.zeros(4 - len(arr)), arr)
    return row_points, arr


def move_field(field, move):
    field = field.copy()
    new_points = 0
    if move == 'up':
        for i in range(len(field)):
            row_points, field[:, i] = move_row(field[:, i][::-1])
            field[:, i] = field[:, i][::-1]
            new_points += row_points
    elif move == 'down':
        for i in range(len(field)):
            row_points, field[:, i] = move_row(field[:, i])
            new_points += row_points
    elif move == 'right':
        for i in range(len(field)):
            row_points, field[i, :] = move_row(field[i, :])
            new_points += row_points
    elif move == 'left':
        for i in range(len(field)):
            row_points, field[i, :] = move_row(field[i, :][::-1])
            field[i, :] = field[i, :][::-1]
            new_points += row_points
    return field, new_points


def field_stucked(field):
    for mv in ['up', 'down', 'right', 'left']:
        fcopy = field.copy()
        fcopy, _ = move_field(fcopy, mv)
        if not np.array_equal(field, fcopy):
            return False
    return True
