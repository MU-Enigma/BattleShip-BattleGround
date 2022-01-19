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

pr.initialize()

while pr.running:
    pr.draw_call()
