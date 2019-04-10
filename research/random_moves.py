from game_logic.moves import *
from research.utils import *
import pandas as pd


def run_random(n_sessions=100, filed_size=4, save_df=False):
    sessions_points = []
    sessions_bests = []
    sessions_moves = []
    if save_df:
        moves_df = list()
        targets_list = list()
    for i in range(n_sessions):
        if save_df:
            sess_moves_df = pd.DataFrame(columns=range(filed_size ** 2))
            sess_targets_list = list()
        points = 0
        num_moves = 0
        field = get_initial_field(filed_size)
        while True:
            move = ['up', 'down', 'right', 'left'][randint(0, 3)]
            if save_df:
                sess_moves_df = sess_moves_df.append(pd.Series(field.flatten(), index=range(filed_size ** 2)),
                                                     ignore_index=True)
                sess_targets_list.append(move)
            field_moved, new_points = move_field(field, move)
            points += new_points
            num_moves += 1
            if not np.array_equal(field_moved, field):
                field = insert_new_cell(field_moved)
            if field_stucked(field):
                sessions_points.append(points)
                sessions_bests.append(np.max(field))
                sessions_moves.append(np.max(num_moves))
                if save_df:
                    moves_df.append(sess_moves_df)
                    targets_list.append(sess_targets_list)
                break
    if save_df:
        return sessions_points, sessions_bests, sessions_moves, moves_df, targets_list
    else:
        return sessions_points, sessions_bests, sessions_moves


# sess_points, sess_bests, sess_moves = run_random()
#
# print('Best score of random action selection: ', str(max(sess_points)))
# print('Highest cell reached: ', str(max(sess_bests)))
# print('Highest num moves : ', str(max(sess_moves)))

# plot_scores(sess_points, 'session points, random')
sess_points, sess_bests, sess_moves, mov_df, tar_list = run_random(n_sessions=2, filed_size=4, save_df=True)

print(sess_points)
print(sess_bests)
print(sess_moves)
print(mov_df)
print(tar_list)
