from game_logic.moves import *
from random import randint

FIELD_SIZE = 4

if __name__ == '__main__':
    points = 0
    field = get_initial_field(FIELD_SIZE)
    while True:
        print('Current points: {}.'.format(points))
        print(field)
        move = input('Enter your move: ')
        while move not in ['up', 'down', 'right', 'left']:
            move = input('Enter your move: ')
        # move = ['up', 'down', 'right', 'left'][randint(0, 3)]  # rand move selection
        field_moved, new_points = move_field(field, move)
        points += new_points
        if not np.array_equal(field_moved, field):
            field = insert_new_cell(field_moved)
        if np.any(field == 2048):
            print('Congrats! 2048 reached!')
        if field_stucked(field):
            print('Thats all folks! Final score: {}.'.format(points))
            break
