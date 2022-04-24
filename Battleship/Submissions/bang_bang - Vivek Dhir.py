import random


class BattleShip:
    def __init__(self):
        self.team_name = "Bang_Bang"
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
        self.special_miss0 = []
        self.special_miss1 = []
        self.hawk_eye = 0
        self.counter = 0

    def set_ships(self):
        return self.ships
    
    def attack(self):
        x = -1
        y = -1

        if self.hawk_eye == 1:
            #hawkeye attack
            for i in range(10):
                self.opponent_board[9][i] = 1
                self.opponent_board[i][9] = 1
                if([9,i] in self.parity):
                    self.parity.remove([9,i])
                if([i,9] in self.parity):
                    self.parity.remove([i,9])
            return (9,9)
        else:
            if self.attack_type == 0:
                if len(self.parity) != 0:
                    rand_elem = random.choice(self.parity)
                    x = rand_elem[0]
                    y = rand_elem[1]
                else:
                    if len(self.special_miss1) != 0:
                        rand_elem = random.choice(self.special_miss1)
                        x = rand_elem[0]
                        y = rand_elem[1]
                        (self.special_miss1).remove([x,y])
                    elif len(self.special_miss0) != 0:
                        rand_elem = random.choice(self.special_miss0)
                        x = rand_elem[0]
                        y = rand_elem[1]
                        (self.special_miss0).remove([x,y])
            elif self.attack_type == 1:
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
            elif self.attack_type == 2:
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
            if([x,y] in self.parity):
                (self.parity).remove([x,y])
            return (x, y)
    
    def hit_or_miss(self, x, y, info):
        self.info = info

        if self.attack_type == 0:
            if info == 0:
                self.opponent_board[x][y] = 0
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
            elif info == 1:
                self.opponent_board[x][y] = 1
                self.special_miss0.append([x,y])
            elif info == 2:
                self.opponent_board[x][y] = 0
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
            elif info == 3:
                self.opponent_board[x][y] = 0
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
                #hawkeye on
                self.hawkeye = 1
        elif self.attack_type == 1:
            if self.hawk_eye == 1:
                self.hawk_eye = 0
                if info == 0:
                    self.opponent_board[x][y] = 0
                    self.attack_type = 2
                    self.fix_direction = self.direction[self.hit_count]
                else:
                    self.special_miss1.append([x,y])
                    self.attack_type = 2
                    self.opponent_board[x][y] = 1
                    self.fix_direction = self.direction[self.hit_count]
            elif info == 0:
                self.opponent_board[x][y] = 0
                self.attack_type = 2
                (self.stack).append([x,y])
                self.fix_direction = self.direction[self.hit_count]
                move = self.fix_direction
                x1 = -1
                y1 = -1
                if(move=='R' and self.stack[-1][1]+1<=9 and self.opponent_board[self.stack[-1][0]][self.stack[-1][1]+1]==-1):
                    x1 = self.stack[-1][0]
                    y1 = self.stack[-1][1]+1
                elif(move=='L'and self.stack[-1][1]-1>=0 and self.opponent_board[self.stack[-1][0]][self.stack[-1][1]-1]==-1):
                    x1 = self.stack[-1][0]
                    y1 = self.stack[-1][1]-1
                elif(move=='U' and self.stack[-1][0]-1>=0 and self.opponent_board[self.stack[-1][0]-1][self.stack[-1][1]]==-1):
                    x1 = self.stack[-1][0]-1
                    y1 = self.stack[-1][1]
                elif(move=='D' and self.stack[-1][0]+1<=9 and self.opponent_board[self.stack[-1][0]+1][self.stack[-1][1]]==-1):
                    x1 = self.stack[-1][0]+1
                    y1 = self.stack[-1][1]
                if x1 == -1 and y1 == -1:
                    #next search point impossible
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
            elif info == 1:
                self.special_miss1.append([x,y])
                self.opponent_board[x][y] = 1
                self.hit_count+=1
                self.fix_direction = self.direction[self.hit_count]
            elif info == 2:
                self.opponent_board[x][y] = 0
                self.attack_type = 2
                (self.stack).append([x,y])
                self.fix_direction = self.direction[self.hit_count]
                move = self.fix_direction
                x1 = -1
                y1 = -1
                if(move=='R' and self.stack[-1][1]+1<=9 and self.opponent_board[self.stack[-1][0]][self.stack[-1][1]+1]==-1):
                    x1 = self.stack[-1][0]
                    y1 = self.stack[-1][1]+1
                elif(move=='L'and self.stack[-1][1]-1>=0 and self.opponent_board[self.stack[-1][0]][self.stack[-1][1]-1]==-1):
                    x1 = self.stack[-1][0]
                    y1 = self.stack[-1][1]-1
                elif(move=='U' and self.stack[-1][0]-1>=0 and self.opponent_board[self.stack[-1][0]-1][self.stack[-1][1]]==-1):
                    x1 = self.stack[-1][0]-1
                    y1 = self.stack[-1][1]
                elif(move=='D' and self.stack[-1][0]+1<=9 and self.opponent_board[self.stack[-1][0]+1][self.stack[-1][1]]==-1):
                    x1 = self.stack[-1][0]+1
                    y1 = self.stack[-1][1]
                if x1 == -1 and y1 == -1:
                    #next search point impossible
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
            elif info == 3:
                self.opponent_board[x][y] = 0
                self.attack_type = 2
                (self.stack).append([x,y])
                self.hawk_eye = 1
                self.fix_direction = self.direction[self.hit_count]
                move = self.fix_direction
                x1 = -1
                y1 = -1
                if(move=='R' and self.stack[-1][1]+1<=9 and self.opponent_board[self.stack[-1][0]][self.stack[-1][1]+1]==-1):
                    x1 = self.stack[-1][0]
                    y1 = self.stack[-1][1]+1
                elif(move=='L'and self.stack[-1][1]-1>=0 and self.opponent_board[self.stack[-1][0]][self.stack[-1][1]-1]==-1):
                    x1 = self.stack[-1][0]
                    y1 = self.stack[-1][1]-1
                elif(move=='U' and self.stack[-1][0]-1>=0 and self.opponent_board[self.stack[-1][0]-1][self.stack[-1][1]]==-1):
                    x1 = self.stack[-1][0]-1
                    y1 = self.stack[-1][1]
                elif(move=='D' and self.stack[-1][0]+1<=9 and self.opponent_board[self.stack[-1][0]+1][self.stack[-1][1]]==-1):
                    x1 = self.stack[-1][0]+1
                    y1 = self.stack[-1][1]
                if x1 == -1 and y1 == -1:
                    #next search point impossible
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
        elif self.attack_type == 2:
            if self.hawk_eye == 1:
                self.hawk_eye = 0
                move = self.fix_direction
                x1 = -1
                y1 = -1
                if(move=='R' and self.stack[-1][1]+1<=9 and self.opponent_board[self.stack[-1][0]][self.stack[-1][1]+1]==-1):
                    x1 = self.stack[-1][0]
                    y1 = self.stack[-1][1]+1
                elif(move=='L'and self.stack[-1][1]-1>=0 and self.opponent_board[self.stack[-1][0]][self.stack[-1][1]-1]==-1):
                    x1 = self.stack[-1][0]
                    y1 = self.stack[-1][1]-1
                elif(move=='U' and self.stack[-1][0]-1>=0 and self.opponent_board[self.stack[-1][0]-1][self.stack[-1][1]]==-1):
                    x1 = self.stack[-1][0]-1
                    y1 = self.stack[-1][1]
                elif(move=='D' and self.stack[-1][0]+1<=9 and self.opponent_board[self.stack[-1][0]+1][self.stack[-1][1]]==-1):
                    x1 = self.stack[-1][0]+1
                    y1 = self.stack[-1][1]
                if x1 == -1 and y1 == -1:
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
                if info == 0:
                    self.opponent_board[x][y] = 0
                    self.fix_direction = self.direction[self.hit_count]
                else:
                    self.special_miss1.append([x,y])
                    self.opponent_board[x][y] = 1
                    self.fix_direction = self.direction[self.hit_count]
            elif info == 0:
                self.opponent_board[x][y] = 0
                (self.stack).append([x,y])
                move = self.fix_direction
                x1 = -1
                y1 = -1
                if(move=='R' and self.stack[-1][1]+1<=9 and self.opponent_board[self.stack[-1][0]][self.stack[-1][1]+1]==-1):
                    x1 = self.stack[-1][0]
                    y1 = self.stack[-1][1]+1
                elif(move=='L'and self.stack[-1][1]-1>=0 and self.opponent_board[self.stack[-1][0]][self.stack[-1][1]-1]==-1):
                    x1 = self.stack[-1][0]
                    y1 = self.stack[-1][1]-1
                elif(move=='U' and self.stack[-1][0]-1>=0 and self.opponent_board[self.stack[-1][0]-1][self.stack[-1][1]]==-1):
                    x1 = self.stack[-1][0]-1
                    y1 = self.stack[-1][1]
                elif(move=='D' and self.stack[-1][0]+1<=9 and self.opponent_board[self.stack[-1][0]+1][self.stack[-1][1]]==-1):
                    x1 = self.stack[-1][0]+1
                    y1 = self.stack[-1][1]
                if x1 == -1 and y1 == -1:
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
            elif info == 1:
                self.special_miss1.append([x,y])
                self.opponent_board[x][y] = 1
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
            elif info == 2:
                self.opponent_board[x][y] = 0
                (self.stack).append([x,y])
                move = self.fix_direction
                x1 = -1
                y1 = -1
                if(move=='R' and self.stack[-1][1]+1<=9 and self.opponent_board[self.stack[-1][0]][self.stack[-1][1]+1]==-1):
                    x1 = self.stack[-1][0]
                    y1 = self.stack[-1][1]+1
                elif(move=='L'and self.stack[-1][1]-1>=0 and self.opponent_board[self.stack[-1][0]][self.stack[-1][1]-1]==-1):
                    x1 = self.stack[-1][0]
                    y1 = self.stack[-1][1]-1
                elif(move=='U' and self.stack[-1][0]-1>=0 and self.opponent_board[self.stack[-1][0]-1][self.stack[-1][1]]==-1):
                    x1 = self.stack[-1][0]-1
                    y1 = self.stack[-1][1]
                elif(move=='D' and self.stack[-1][0]+1<=9 and self.opponent_board[self.stack[-1][0]+1][self.stack[-1][1]]==-1):
                    x1 = self.stack[-1][0]+1
                    y1 = self.stack[-1][1]
                if x1 == -1 and y1 == -1:
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
            elif info == 3:
                self.opponent_board[x][y] = 0
                (self.stack).append([x,y])
                self.hawk_eye = 1
                move = self.fix_direction
                x1 = -1
                y1 = -1
                if(move=='R' and self.stack[-1][1]+1<=9 and self.opponent_board[self.stack[-1][0]][self.stack[-1][1]+1]==-1):
                    x1 = self.stack[-1][0]
                    y1 = self.stack[-1][1]+1
                elif(move=='L'and self.stack[-1][1]-1>=0 and self.opponent_board[self.stack[-1][0]][self.stack[-1][1]-1]==-1):
                    x1 = self.stack[-1][0]
                    y1 = self.stack[-1][1]-1
                elif(move=='U' and self.stack[-1][0]-1>=0 and self.opponent_board[self.stack[-1][0]-1][self.stack[-1][1]]==-1):
                    x1 = self.stack[-1][0]-1
                    y1 = self.stack[-1][1]
                elif(move=='D' and self.stack[-1][0]+1<=9 and self.opponent_board[self.stack[-1][0]+1][self.stack[-1][1]]==-1):
                    x1 = self.stack[-1][0]+1
                    y1 = self.stack[-1][1]
                if x1 == -1 and y1 == -1:
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
[1 ,1 ,5 ,1],
[7 ,8 ,3 ,0],
[2 ,3 ,5 ,0],
[6 ,0 ,4 ,0],
[0 , 6 ,4 ,0],]

parity = []
temp = 1
for i in range(10):
    temp = 1 - temp
    for j in range(10):
        if(temp==1):
            parity.append([i,j])
        temp = 1 - temp

opponent_board = []
for i in range(10):
    lis = []
    for j in range(10):
        lis.append(-1)
    opponent_board.append(lis)