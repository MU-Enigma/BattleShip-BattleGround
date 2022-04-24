import random


class BattleShip:
    def __init__(self):
        self.team_name = "Bang"
        self.ships = ships
        self.opponent_board = opponent_board
        self.info = -1
        self.attack_type = 0 # 0 for parity,  1 for hunt and 2 for finish
        self.stack = []
        self.parity = parity
        self.hit_count = 0
        self.fix_direction = ""
        self.attack_status = "partial"
        self.direction = ['R', 'U', 'L', 'D']

    def set_ships(self):
        return self.ships

    def attack(self):
        x = -1
        y = -1
        if(self.info==3):
            for i in range(10):
                self.opponent_board[9][i] = 1
                self.opponent_board[i][9] = 1
                if([9,i] in parity):
                    self.parity.remove([9,i])
                if([i,9] in parity):
                    self.parity.remove([i,9])
            return (9,9)

        if(self.attack_type==0):# 0 for parity,  1 for hunt and 2 for finish
            rand_elem = random.choice(parity) 
            (self.parity).remove(rand_elem)
            x = rand_elem[0]
            y = rand_elem[1]
        if(self.attack_type==1):
            print(self.info)
            print(self.attack_type)
            print(self.attack_status)
            print(self.direction)
            print(self.stack)
            print(self.fix_direction)
            move = self.fix_direction
            if(move=='R' and self.stack[-1][1]+1<=9 and self.opponent_board[self.stack[-1][0]][self.stack[-1][1]+1]==-1):
                x = self.stack[-1][0]
                y = self.stack[-1][1]+1
            elif(move=='L'and self.stack[-1][1]-1>=0 and self.opponent_board[self.stack[-1][0]][self.stack[-1][1]-1]==-1):
                x = self.stack[-1][0]
                y = self.stack[-1][1]-1
            elif(move=='U' and self.stack[-1][0]-1>=0 and self.opponent_board[self.stack[-1][0]-1][self.stack[-1][1]]==-1):
                x = self.stack[-1][0]-1
                y = self.stack[-1][1]
            elif(move=='D' and self.stack[-1][0]+1<=9 and self.opponent_board[self.stack[-1][0]+1][self.stack[-1][1]]==-1):
                x = self.stack[-1][0]+1
                y = self.stack[-1][1]
        if(self.attack_type==2):
            if(self.fix_direction=='L'):
                x = self.stack[-1][0]
                y = self.stack[-1][1]-1
            elif(self.fix_direction=='R'):
                x = self.stack[-1][0]
                y = self.stack[-1][1]+1
            elif(self.fix_direction=='U'):
                x = self.stack[-1][0]-1
                y = self.stack[-1][1]
            elif(self.fix_direction=='D'):
                x = self.stack[-1][0]+1
                y = self.stack[-1][1]
            print(self.info)
            print(self.attack_type)
            print(self.attack_status)
            print(self.direction)
            print(self.stack)
            print(self.fix_direction)

        if([x,y] in self.parity):
            (self.parity).remove([x,y])
        
        return (x, y)


    def hit_or_miss(self, x, y, info):
        if(info==2):
            info = 0
        self.info = info

        # info = 1 for miss, 0 for a hit, -1 for an out of range shooting, 2 for special move nullify. 3 for your next move to be a Hawkeye Shot
        if info != -1:
            self.opponent_board[x][y] = info

        if self.attack_type==1 and info==1: # 0 for parity,  1 for hunt and 2 for finish
            self.hit_count+=1
            self.fix_direction = self.direction[self.hit_count]

        if info == 0 and self.attack_type == 0:
            self.attack_type = 1
            (self.stack).append([x, y]) 
            if(y-1<0 or self.opponent_board[x][y-1]!=-1):
                self.direction.remove('L')
            if(y+1>9 or self.opponent_board[x][y+1]!=-1):
                self.direction.remove('R')
            if(x-1<0  or self.opponent_board[x-1][y]!=-1):
                self.direction.remove('U')
            if(x+1>9 or self.opponent_board[x+1][y]!=-1):
                self.direction.remove('D')
            self.fix_direction = self.direction[self.hit_count]

        elif info == 0 and self.attack_type==1:
            self.attack_type = 2
            (self.stack).append([x,y])
            self.fix_direction = self.direction[self.hit_count]
        elif info == 0 and self.attack_type==2:
            (self.stack).append([x,y])            

        if info == 1 and self.attack_type == 2:
            if(self.attack_status=="partial"):
                fix = False
                self.attack_status = "complete"
                pivot = self.stack[0]
                self.stack = [pivot]
                if(self.fix_direction=="L"):
                    if('R' in self.direction):
                        self.fix_direction = "R"
                        fix = True
                elif(self.fix_direction=="R"):
                    if('L' in self.direction):
                        self.fix_direction = "L"
                        fix = True
                elif(self.fix_direction=="U"):
                    if('D' in self.direction):
                        self.fix_direction = "D"
                        fix = True
                elif(self.fix_direction=="D"):
                    if('U' in self.direction):
                        self.fix_direction = "U"
                        fix = True

                if(not fix):
                    self.attack_type = 0
                    self.stack = []
                    self.hit_count = 0
                    self.fix_direction = ""
                    self.attack_status = "partial"
                    self.direction = ['R', 'U', 'L', 'D']

            elif(self.attack_status == "complete"):
                self.attack_type = 0 # 0 for parity,  1 for hunt and 2 for finish
                self.stack = []
                self.hit_count = 0
                self.fix_direction = ""
                self.attack_status = "partial"
                self.direction = ['R', 'U', 'L', 'D']

ships = [
 [3, 3, 3, 1],
 [4, 3, 4, 0],
 [5, 8, 4, 0],
 [1, 1, 5, 1],
 [9, 1, 5, 1], ]

parity_board = []
p = 0
for i in range(10):
    temp = []
    for j in range(10):
        temp.append(p)
        p = 1 - p
    parity_board.append(temp)
    p = 1-p
print(parity_board)

parity = []
for i in range(10):
    for j in range(10):
        if(parity_board[i][j]==1):
            parity.append([i,j])

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