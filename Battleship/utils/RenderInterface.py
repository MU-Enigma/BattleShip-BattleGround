import PygameRenderer as pr

"""
for board matrix use the following convention:
0 - water
1 - ship
2 - destroyed ship
3 - special regions
"""

pr.max_board_dim = [400, 400]
pr.side_column_width = 0
pr.leaderboard_height = 0

# Can override margins/thickness here





# Dummy Values for testing purposes
board1 = [[0, 0, 0, 0, 0, 0, 0, 0],
          [0, 1, 1, 1, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0]]
board2 = [[0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0]]


board1_ships = [
  [1, 1, 0, 3, 1] # ship entry format: [board_pos_x, board_pos_y, orientation (right(1), down(-1)), size_x (in board units not pixels), size_y]
]
board2_ships = []



def initialize(Board1_ships, Board2_ships):
    # Make sure ship lists are legal.
    pr.board1 = board1
    pr.board2 = board2
    pr.ships1 = Board1_ships
    pr.ships2 = Board2_ships
    pr.initialize()

def run():
    while pr.running:
        pr.draw_call()


initialize(board1_ships, board2_ships)
pr.initialize()
run()
