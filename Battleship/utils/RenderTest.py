from . import PygameRenderer as pr

"""
for board matrix use the following convention:
0 - water
1 - ship
2 - destroyed ship
3 - special regions
"""

pr.max_board_dim = [400, 400]
pr.side_column_width = 100
pr.leaderboard_height = 200

# Can override margins/thickness here

board1 = []
board2 = []


def initialize():
    pr.board1 = board1
    pr.board2 = board2
    pr.initialize()

def update(b1, b2):
    global board1, board2
    print(b1)
    pr.board1 = b1
    pr.board2 = b2
    pr.draw_call(pr.board1, pr.board2)

def run():
    while pr.running:
        pr.draw_call(pr.board1, pr.board2)
