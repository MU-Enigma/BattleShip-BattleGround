import random

class BattleShip:
    def __init__(self):
        self.team_name = "Team 2"
        self.board = board
        self.opponent_board = opponent_board
        self.info = -1

    def set_board(self):
        return self.board

    def attack(self):
        x = random.randint(0,1)
        y = random.randint(0,3)
        print("TEAM 1 : " ,self.info)
        return (x,y)

    def hit_or_miss(self, x, y , info):
        self.info = info
        self.opponent_board[x][y] = info



board = [
        [1 , 1 , 0, 0],
        [0 , 0 , 0, 0]
    ]


opponent_board = [
        [-1 , -1 , -1 , -1],
        [-1 , -1 , -1 , -1]
    ]

