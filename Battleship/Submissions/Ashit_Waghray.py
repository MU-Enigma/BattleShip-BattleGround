import random

class BattleShip:
    def __init__(self):
        self.team_name = "Ashit ih"
        self.ships = ships
        self.opponent_board = opponent_board
        self.info = -1
        self.turn_count = 0
        self.x = x
        self.y = y
        self.hawkeye = 0
        self.upalabdh_ships = [5,5,4,4,3]
        self.hit_count = 0

    def set_ships(self):
        return self.ships

    def addition(self, lis1, lis2):
        for i in range(len(lis1)):
            for j in range(len(lis2[i])):
                lis1[i][j] += lis2[i][j]
        return lis1
    def amax(self, lis):
        x = -1000000
        for i in lis:
            for j in i:
                x = max(x, j)
        return x

    def where(self, lis, amaxi):
        l1 = []
        l2 = []
        for i in range(len(lis)):
            for j in range(len(lis[i])):
                if (lis[i][j]==amaxi):
                    l1.append(i)
                    l2.append(j)
        return [l1, l2]

    def HeatmapGenerator(self,ship):
        opponent_board_heat = [
            [0,0,0,0,0,0,0,0,0,0]
            ,[0,0,0,0,0,0,0,0,0,0]
            ,[0,0,0,0,0,0,0,0,0,0]
            ,[0,0,0,0,0,0,0,0,0,0]
            ,[0,0,0,0,0,0,0,0,0,0]
            ,[0,0,0,0,0,0,0,0,0,0]
            ,[0,0,0,0,0,0,0,0,0,0]
            ,[0,0,0,0,0,0,0,0,0,0]
            ,[0,0,0,0,0,0,0,0,0,0]
            ,[0,0,0,0,0,0,0,0,0,0]]
        
        
        goodx = 0
        goody = 0
        H1 = 0
        while H1 < 10:
            H2 = 0
            while H2 < 10:
                if self.opponent_board[H1][H2] != 1 and self.opponent_board[H1][H2] != 8:
                    if 9 - H2 >= (ship-1):
                        for x in range(ship):
                            if self.opponent_board[H1][H2+x] != 1 and self.opponent_board[H1][H2+x] != 8:
                                goodx += 1
                            else:
                                goodx -= 100
                            if self.opponent_board[H1][H2+x] == 0:
                                goodx += 10
                        if goodx > 0:    
                            for z in range(ship):
                                opponent_board_heat[H1][H2+z] += 1
                        if goodx > 10:
                            for z in range(ship):
                                opponent_board_heat[H1][H2+z] += 100
                    if self.opponent_board[H1][H2] == 0:
                        opponent_board_heat[H1][H2] -= 10000
                H2 += 1
                goodx = 0
            H1 += 1
        
        H2 = 0
        while H2 < 10:
            H1 = 0
            while H1 < 10:
                if self.opponent_board[H1][H2] != 1 and self.opponent_board[H1][H2] != 8:
                    if 9 - H1 >= (ship-1):
                        for x in range(ship):
                            if self.opponent_board[H1+x][H2] != 1 and self.opponent_board[H1+x][H2] != 8:
                                goody += 1
                            else:
                                goody -= 100
                            if self.opponent_board[H1+x][H2] == 0:
                                goody += 10
                        if goody > 0:
                            for z in range(ship):
                                opponent_board_heat[H1+z][H2] += 1
                        if goody > 10:
                            for z in range(ship):
                                opponent_board_heat[H1+z][H2] += 100
                    if self.opponent_board[H1][H2] == 0:
                        opponent_board_heat[H1][H2] -= 10000
                H1 += 1
                goody = 0
            H2 += 1
                
        return opponent_board_heat

    def attack(self):
        if self.hawkeye == 0:
            Heatmap_ALL = [
            [0,0,0,0,0,0,0,0,0,0]
            ,[0,0,0,0,0,0,0,0,0,0]
            ,[0,0,0,0,0,0,0,0,0,0]
            ,[0,0,0,0,0,0,0,0,0,0]
            ,[0,0,0,0,0,0,0,0,0,0]
            ,[0,0,0,0,0,0,0,0,0,0]
            ,[0,0,0,0,0,0,0,0,0,0]
            ,[0,0,0,0,0,0,0,0,0,0]
            ,[0,0,0,0,0,0,0,0,0,0]
            ,[0,0,0,0,0,0,0,0,0,0]]
            
            for i in self.upalabdh_ships:
                Heatmap_ALL = self.addition(Heatmap_ALL,self.HeatmapGenerator(i))
            next_guess = self.where(Heatmap_ALL, self.amax(Heatmap_ALL))
            next_coordinates = list(zip(next_guess[0],next_guess[1]))
            First = (next_coordinates[random.randint(1,len(next_coordinates))-1])
            self.x = First[0]
            self.y = First[1]
        else:
            self.x = 0
            self.y = 0
            for i in range(10):
                self.opponent_board[0][i] = 1
                self.opponent_board[i][0] = 1
            self.hawkeye = 0
        return (self.x,self.y)

    def hit_or_miss(self, x, y , info):
        self.info = info
        ## info = 1 for miss, 0 for a hit, -1 for an out of range shooting, 2 for special move nullify. 3 for your next move to be a Hawkeye Shot
        if info == 0:
            self.opponent_board[x][y] = 0
            self.hit_count += 1
            if self.hit_count in self.upalabdh_ships:
                self.upalabdh_ships.remove(self.hit_count)
                self.hit_count = 0
        elif info == 1:
            self.opponent_board[x][y] = 1
        elif info == 2:
            self.opponent_board[x][y] = 0
            self.hit_count += 1
            if self.hit_count in self.upalabdh_ships:
                self.upalabdh_ships.remove(self.hit_count)
                self.hit_count = 0
        elif info == 3:
            self.opponent_board[x][y] = 0
            self.hawkeye = 1
            self.hit_count += 1
            if self.hit_count in self.upalabdh_ships:
                self.upalabdh_ships.remove(self.hit_count)
                self.hit_count = 0

x = 0
y = 0

ships = [
[1 ,1 ,5 ,1],
[7 ,8 ,3 ,0],
[2 ,3 ,5 ,0],
[6 ,0 ,4 ,0],
[0 , 6 ,4 ,0],]

opponent_board = []
for i in range(10):
    lis = []
    for j in range(10):
        lis.append(-1)
    opponent_board.append(lis)