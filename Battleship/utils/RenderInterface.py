import PygameRenderer as pr
import time

"""
for board matrix use the following convention:
0 - water
1 - ship
2 - destroyed ship
3 - special regions
"""

pr.max_board_dim = [800, 800]
pr.side_column_width = 0
pr.leaderboard_height = 0

# Can override margins/thickness here

# Internal Timer.
start_time = time.time()

#TimeLine
initial_skirting = 0.5



# Dummy Values for testing purposes
board1 = [[0, 0, 0, 0, 0, 0, 1, 0],
          [0, 1, 1, 1, 0, 0, 1, 0],
          [0, 0, 0, 0, 0, 0, 1, 0],
          [0, 0, 0, 1, 1, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0]]

board2 = [[0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 1, 0, 0, 0],
          [1, 1, 1, 0, 1, 0, 0, 0],
          [1, 1, 1, 0, 1, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 1, 1]]


board1_ships = [
    [1, 1, 0, 3, 1], # ship entry format: [board_pos_x, board_pos_y, orientation (right(0) or horizontal, down(-1) or vertical), size_x (in board units not pixels), size_y]
    [6, 0, -1, 1, 3],
    [3, 3, 0, 2, 1]
]
board2_ships = [
    [4, 1, -1, 1, 3],
    [0, 2, 0, 3, 2],
    [6, 4, 0, 2, 1]
]



def initialize(Board1_ships, Board2_ships):
    # Make sure ship lists are legal.
    pr.board1 = board1
    pr.board2 = board2
    pr.ships1 = Board1_ships
    pr.ships2 = Board2_ships
    pr.initialize()


initialize(board1_ships, board2_ships)
while pr.running:
    time_elapsed = time.time()-start_time
    if time_elapsed < initial_skirting:
        pr.draw_call([None, None])
    else:
        pr.draw_call(['strike', [2, 2, 2]]) # strike animation takes board_num, board_pos_x, board_pos_y
