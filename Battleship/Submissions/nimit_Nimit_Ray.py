import random

class BattleShip:
    def __init__(self):
        self.team_name = "Bang Bang Bang"
        self.ships = ships
        self.opponent_board = opponent_board
        self.info = -1
        self.board = board
        self.turn_count = 0
        self.x = x
        self.y = y
        self.hawkeye = 0

    def set_ships(self):
        return self.ships

    def attack(self):
        if self.hawkeye == 0:
            rand_elem = random.choice(self.board)
            self.x = rand_elem[0]
            self.y = rand_elem[1]

            if [self.x,self.y] in self.board:
                (self.board).remove([self.x,self.y])
        else:
            self.x = 9
            self.y = 9
            for i in range(10):
                self.opponent_board[9][i] = 1
                self.opponent_board[i][9] = 1
                if([9,i] in self.board):
                    self.board.remove([9,i])
                if([i,9] in self.board):
                    self.board.remove([i,9])
        return (self.x,self.y)

    def hit_or_miss(self, x, y , info):
        self.info = info
        ## info = 1 for miss, 0 for a hit, -1 for an out of range shooting, 2 for special move nullify. 3 for your next move to be a Hawkeye Shot
        if info == 0:
            self.opponent_board[x][y] = 0
        elif info == 1:
            self.opponent_board[x][y] = 1
        elif info == 2:
            self.opponent_board[x][y] = 0
        elif info == 3:
            self.opponent_board[x][y] = 0
            self.hawkeye = 1

x = 0
y = 0

ships = [
[1 ,1 ,5 ,1],
[7 ,8 ,3 ,0],
[2 ,3 ,5 ,0],
[6 ,0 ,4 ,0],
[0 , 6 ,4 ,0],]

board = []
temp = 1
for i in range(10):
    for j in range(10):
        board.append([i,j])

opponent_board = []
for i in range(10):
    lis = []
    for j in range(10):
        lis.append(-1)
    opponent_board.append(lis)