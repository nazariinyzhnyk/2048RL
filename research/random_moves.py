from game_logic.moves import *

FIELD_SIZE = 4
N_SESSIONS = 1000

sessions_points = []
sessions_bests = []
if __name__ == '__main__':
    for i in range(N_SESSIONS):
        points = 0
        field = get_initial_field(FIELD_SIZE)
        while True:
            move = ['up', 'down', 'right', 'left'][randint(0, 3)]
            field_moved, new_points = move_field(field, move)
            points += new_points
            if not np.array_equal(field_moved, field):
                field = insert_new_cell(field_moved)
            if field_stucked(field):
                sessions_points.append(points)
                sessions_bests.append(np.max(field))
                break

print('Best score of random action selection: ', str(max(sessions_points)))
print('Highest cell reached: ', str(max(sessions_bests)))
