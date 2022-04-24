import random

class BattleShip:
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

    randomG = [
            (4,1),(0,2),(0,4),(0,7),
            (1,1),(1,7),
            (2,0),(2,8),(2,9),
            (3,4),(3,8),
            (4,0),(4,3),(4,5),
            (5,4),(5,6),(5,9),
            (6,1),(6,5),(6,8)
            (7,0),(7,1),(7,8),(7,9),
            (8,2),(8,8),
            (9,1),(9,2),(9,3),(9,4),(9,5),(9,6),(9,7),(9,8),(9,9)
        ]
    randomIndex = 0
    initial = [4,1]
    diamond = True #Weather we are still in diamond
    hits = []
    hit_index = 0
    def __init__(self):
        self.team_name = "bhoom"
        self.ships = self.set_ships()
        self.opponent_board = self.opponent_board
        self.info = -1

    def set_ships(self):
        self.ships = [
            [2, 0, 5, 1],
            [0, 9, 5, 0],
            [5, 2, 4, 0],
            [7, 5, 4, 1],
            [9, 1, 3, 1]
        ]
        return self.ships

    def attack(self):
        if self.initial != [5,2] and self.diamond == True:
            if(self.initial[0]>1 and self.initial[0]<=4 and self.initial[1]<4):
                self.initial[0]-=1
                self.initial[1]+=1
            elif(self.initial[0]>=1 and self.initial[0]<=4 and self.initial[1]>=4):
                self.initial[0]+=1
                self.initial[1]+=1
            elif(self.initial[0]>=5  and self.initial[1]>=6):
                self.initial[0]+=1
                self.initial[1]-=1
            elif(self.initial[0]>4 and self.initial[1]<=5):
                self.initial[0]-=1
                self.initial[1]-=1
            return self.initial
        elif self.initial == [5,2]:
            self.diamond = False
        


        if(len(self.hits)!=0 and self.hit_index<len(self.hits)):
            x, y = self.hits[self.hit_index]
            res = (0,0)
            if x < 9 and self.opponent_board[x+1][y]==0:
                if(x > 0 and self.opponent_board[x-1][y]==-1):
                    return (x-1,y)
            elif(x < 9 and self.opponent_board[x+1][y]==-1 and (y<9 and y > 0) and (self.opponent_board[x][y+1] != 0 and self.opponent_board[x][y-1] != 0)):
                res = (x+1,y)
            
                    # elif x>0 and self.opponent_board[x-1][y]==0:
                        
            if x >0 and self.opponent_board[x-1][y]==0:
                if(x < 9 and self.opponent_board[x+1][y]==-1):
                    return (x+1,y)
            elif(x>0 and self.opponent_board[x-1][y]==-1 and (y<9 and y > 0) and (self.opponent_board[x][y+1] != 0 and self.opponent_board[x][y-1] != 0)):
                res = (x-1,y)
            


            if y < 9 and self.opponent_board[x][y+1]==0:
                if( y >0 and self.opponent_board[x][y-1]==-1):
                    return (x,y-1)
            elif(y < 9 and self.opponent_board[x][y+1]==-1 and (x<9 and x > 0) and (self.opponent_board[x+1][y] != 0 and self.opponent_board[x-1][y] != 0)):
                res = (x,y+1)
            


            if(y>0 and self.opponent_board[x][y-1]==0):
                if(y<9 and self.opponent_board[x][y+1]==-1):
                    return (x,y+1)
            elif(y>0 and self.opponent_board[x][y-1]==-1 and (x<9 and x > 0) and (self.opponent_board[x+1][y] != 0 and self.opponent_board[x-1][y] != 0)):
                res = (x,y-1)
            
            if res == (0,0):
                self.hit_index+=1
                return self.attack()
            
            
            # self.hit_index+=1
            return res
        
        else: #length of hits is 0
            while self.randomIndex < len(self.randomG):
                sq = self.randomG[self.randomIndex]
                self.randomIndex+=1
                if self.opponent_board[sq[0]][sq[1]] == -1:
                    return sq
                else:
                    self.randomIndex+=1

        for r in range(10):
            for c in range(10):
                if self.opponent_board[r][c] == -1:
                    return (r,c)
        
        return (0,0)
    
        

    def hit_or_miss(self, x, y , info):
        self.info = info
        if(self.info == 0): #meaning it was a hit
            self.hits.append((x,y))
            # if self.diamond == False:
            #     self.hit_index+=1
        ## info = 1 for miss, 0 for a hit, -1 for an out of range shooting, 2 for special move nullify. 3 for your next move to be a Hawkeye Shot
        if info != -1 and info == 0:
            self.opponent_board[x][y] = info
        if info == 1:
            self.opponent_board[x][y] = info

