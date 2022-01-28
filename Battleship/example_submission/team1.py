import random

class BattleShip:
    def __init__(self):
        self.team_name = "Team 1"
        self.board = board
        self.opponent_board = opponent_board
        self.info = -1

    def set_board(self):
        return self.board

    def attack(self):
        x = random.randint(0,10)
        y = random.randint(0,10)
        return (x,y)

    def hit_or_miss(self, x, y , info):
        self.info = info
        ## info = 1 for miss, 0 for a hit, -1 for an out of range shooting
        if info != -1 and info == 0:
            self.opponent_board[x][y] = info



board = [
        [1 , 1 , 0, 0, 1 , 0, 0, 1, 0, 1],
        [0 , 1 , 0, 0, 1 , 1 , 0, 0, 1, 0],
        [0 , 1 , 0, 0, 1 , 0 , 0, 0, 1, 1],
        [0 , 1 , 0, 0, 1 , 1 , 0, 0, 0, 1],
        [1 , 1 , 1, 1, 1 , 1 , 1, 1, 1, 1],
        [0 , 1 , 0, 0, 1 , 0 , 0, 1, 0, 1],
        [0 , 1 , 0, 0, 1 , 0 , 0, 0, 0, 1],
        [0 , 1 , 0, 0, 1 , 1 , 0, 0, 1, 0],
        [0 , 1 , 0, 0, 1 , 1 , 0, 0, 1, 1],
        [0 , 1 , 0, 0, 1 , 1 , 0, 0, 0, 1],
    ]

# board = [
#         [1 , 1 , 0, 0, 1, 1],
#         [0 , 1 , 1, 0, 1, 1],
#         [0 , 1 , 0, 1, 0 ,0],
#         [0 , 1 , 1, 1, 1 ,1],
#         [0 , 0 , 0, 0, 1 ,1],
#         [0 , 0 , 0, 0, 0, 0]
#     ]


opponent_board = [
        [-1 , -1 , -1 , -1 , -1 , -1 , -1 , -1 , -1 , -1],
        [-1 , -1 , -1 , -1 , -1 , -1 , -1 , -1 , -1 , -1],
        [-1 , -1 , -1 , -1 , -1 , -1 , -1 , -1 , -1 , -1],
        [-1 , -1 , -1 , -1 , -1 , -1 , -1 , -1 , -1 , -1],
        [-1 , -1 , -1 , -1 , -1 , -1 , -1 , -1 , -1 , -1],
        [-1 , -1 , -1 , -1 , -1 , -1 , -1 , -1 , -1 , -1],
        [-1 , -1 , -1 , -1 , -1 , -1 , -1 , -1 , -1 , -1],
        [-1 , -1 , -1 , -1 , -1 , -1 , -1 , -1 , -1 , -1],
        [-1 , -1 , -1 , -1 , -1 , -1 , -1 , -1 , -1 , -1],
        [-1 , -1 , -1 , -1 , -1 , -1 , -1 , -1 , -1 , -1],
    ]

