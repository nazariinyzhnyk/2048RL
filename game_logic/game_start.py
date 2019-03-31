from moves import *

FIELD_SIZE = 4

if __name__ == '__main__':
    points = 0
    field = get_initial_field(FIELD_SIZE)
    if np.any(field == 2048):
        print('Congrats! 2048 reached!')
    if field_stucked(field):
        print('Thats all folks! Final score: {}.'.format(points))
    print(field)
