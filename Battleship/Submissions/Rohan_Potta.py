import random

to_hits = []

gonna_left = [] #check left
gonna_right = [] #check Right
gonna_up = [] #check up
gonna_down = [] #check down

for i in range(10):
    for j in range(10):
        to_hits.append([i,j]) 

 
def left(x,y):
    for i in range(1,5): 
        if (y-i<0):
            continue
        to_hits.insert(0,[x,y-i])

def right(x,y):
    for i in range(1,5):
        if (y+i>9):
            continue
        to_hits.insert(0,[x,y+i])

def up(x,y):
    for i in range(1,5):
        if (x-i<0):
            continue
        to_hits.insert(0,[x-i,y])
def down(x,y):
    for i in range(1,5):
        if (x+i>9):
            continue
        to_hits.insert(0,[x+i,y])

class BattleShip:
    def __init__(self):
        self.team_name = "10K "
        self.ships = ships
        self.opponent_board = opponent_board
        self.info = -1

    def set_ships(self):
        return self.ships

    def attack(self):
        x =  to_hits[0][0]#first index x value
        y = to_hits[0][1]# first index y value
        to_hits.pop(0) #removes the index value 
        return (x,y) #return x,y to hit next



    def hit_or_miss(self, x, y, info):
        self.info = info
        # info = 1 for miss, 0 for a hit, -1 for an out of range shooting, 2 for special move nullify. 3 for your next move to be a Hawkeye Shot
        if info != -1 and info == 0:
            self.opponent_board[x][y] = info



ships = [
        [0,5,3,1],
        [1,9,4,0],
        [3,0,5,0],
        [7,6,4,1],
        [9,5,5,1]
        ]


opponent_board = [
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
]

