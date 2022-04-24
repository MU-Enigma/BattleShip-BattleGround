import random

class BattleShip:
    def __init__(self):
        self.team_name = "The High Table"
        self.ships = ships
        self.enemy_board = enemy_board
        self.info = -1
        self.dadi_rakam = 0 
        self.dabba = []
        self.dadi_lekka = 0
        self.anukunna_disa = 0
        self.dadi_sthiti = 0
        self.disa = [2, -2, 1, -1]
        self.dega_kannu = 0
        self.akada = 0
        self.migilipoina_ships = [5,5,4,4,3]
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
        # enemy_board_heat = numpy.array(
        #     [[0,0,0,0,0,0,0,0,0,0]
        #     ,[0,0,0,0,0,0,0,0,0,0]
        #     ,[0,0,0,0,0,0,0,0,0,0]
        #     ,[0,0,0,0,0,0,0,0,0,0]
        #     ,[0,0,0,0,0,0,0,0,0,0]
        #     ,[0,0,0,0,0,0,0,0,0,0]
        #     ,[0,0,0,0,0,0,0,0,0,0]
        #     ,[0,0,0,0,0,0,0,0,0,0]
        #     ,[0,0,0,0,0,0,0,0,0,0]
        #     ,[0,0,0,0,0,0,0,0,0,0]]
        #     )
        enemy_board_heat = [
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
                if self.enemy_board[H1][H2] != 1 and self.enemy_board[H1][H2] != 8:
                    if 9 - H2 >= (ship-1):
                        for x in range(ship):
                            if self.enemy_board[H1][H2+x] != 1 and self.enemy_board[H1][H2+x] != 8:
                                goodx += 1
                            else:
                                goodx -= 100
                            if self.enemy_board[H1][H2+x] == 0:
                                goodx += 10
                        if goodx > 0:    
                            for z in range(ship):
                                enemy_board_heat[H1][H2+z] += 1
                        if goodx > 10:
                            for z in range(ship):
                                enemy_board_heat[H1][H2+z] += 100
                    if self.enemy_board[H1][H2] == 0:
                        enemy_board_heat[H1][H2] -= 10000
                H2 += 1
                goodx = 0
            H1 += 1
        
        H2 = 0
        while H2 < 10:
            H1 = 0
            while H1 < 10:
                if self.enemy_board[H1][H2] != 1 and self.enemy_board[H1][H2] != 8:
                    if 9 - H1 >= (ship-1):
                        for x in range(ship):
                            if self.enemy_board[H1+x][H2] != 1 and self.enemy_board[H1+x][H2] != 8:
                                goody += 1
                            else:
                                goody -= 100
                            if self.enemy_board[H1+x][H2] == 0:
                                goody += 10
                        if goody > 0:
                            for z in range(ship):
                                enemy_board_heat[H1+z][H2] += 1
                        if goody > 10:
                            for z in range(ship):
                                enemy_board_heat[H1+z][H2] += 100
                    if self.enemy_board[H1][H2] == 0:
                        enemy_board_heat[H1][H2] -= 10000
                H1 += 1
                goody = 0
            H2 += 1
                
        return enemy_board_heat

    def attack(self):
        x = -1
        y = -1

        if self.dega_kannu == 1:
            #hawkeye attack
            for i in range(10):
                self.enemy_board[9][i] = 1
                self.enemy_board[i][9] = 1
            return (9,9)
        else:
            if self.dadi_rakam == 0:
                #make heatmap using available_ships
                # Heatmap_ALL = numpy.array(
                # [[0,0,0,0,0,0,0,0,0,0]
                # ,[0,0,0,0,0,0,0,0,0,0]
                # ,[0,0,0,0,0,0,0,0,0,0]
                # ,[0,0,0,0,0,0,0,0,0,0]
                # ,[0,0,0,0,0,0,0,0,0,0]
                # ,[0,0,0,0,0,0,0,0,0,0]
                # ,[0,0,0,0,0,0,0,0,0,0]
                # ,[0,0,0,0,0,0,0,0,0,0]
                # ,[0,0,0,0,0,0,0,0,0,0]
                # ,[0,0,0,0,0,0,0,0,0,0]]
                # )
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
                
                for i in self.migilipoina_ships:
                    Heatmap_ALL = self.addition(Heatmap_ALL,self.HeatmapGenerator(i))
                next_guess = self.where(Heatmap_ALL, self.amax(Heatmap_ALL))
                next_coordinates = list(zip(next_guess[0],next_guess[1]))
                First = (next_coordinates[random.randint(1,len(next_coordinates))-1])
                x = First[0]
                y = First[1]
            elif self.dadi_rakam == 1:
                move = self.anukunna_disa
                if(move==2 and self.dabba[-1][1]+1<=9 and self.enemy_board[self.dabba[-1][0]][self.dabba[-1][1]+1]==-1):
                    x = self.dabba[-1][0]
                    y = self.dabba[-1][1]+1
                elif(move==1 and self.dabba[-1][1]-1>=0 and self.enemy_board[self.dabba[-1][0]][self.dabba[-1][1]-1]==-1):
                    x = self.dabba[-1][0]
                    y = self.dabba[-1][1]-1
                elif(move==-2 and self.dabba[-1][0]-1>=0 and self.enemy_board[self.dabba[-1][0]-1][self.dabba[-1][1]]==-1):
                    x = self.dabba[-1][0]-1
                    y = self.dabba[-1][1]
                elif(move==-1 and self.dabba[-1][0]+1<=9 and self.enemy_board[self.dabba[-1][0]+1][self.dabba[-1][1]]==-1):
                    x = self.dabba[-1][0]+1
                    y = self.dabba[-1][1]
            elif self.dadi_rakam == 2:
                if(self.anukunna_disa==1):
                    x = self.dabba[-1][0]
                    y = self.dabba[-1][1]-1
                elif(self.anukunna_disa==2):
                    x = self.dabba[-1][0]
                    y = self.dabba[-1][1]+1
                elif(self.anukunna_disa==-2):
                    x = self.dabba[-1][0]-1
                    y = self.dabba[-1][1]
                elif(self.anukunna_disa==-1):
                    x = self.dabba[-1][0]+1
                    y = self.dabba[-1][1]
            return (x, y)
    
    def hit_or_miss(self, x, y, info):
        self.info = info

        if self.dadi_rakam == 0:
            if info == 0:
                self.akada += 1
                self.enemy_board[x][y] = 0
                self.dadi_rakam = 1
                (self.dabba).append([x, y]) 
                if(y-1<0 or self.enemy_board[x][y-1]!=-1):
                    self.disa.remove(1)
                if(y+1>9 or self.enemy_board[x][y+1]!=-1):
                    self.disa.remove(2)
                if(x-1<0  or self.enemy_board[x-1][y]!=-1):
                    self.disa.remove(-2)
                if(x+1>9 or self.enemy_board[x+1][y]!=-1):
                    self.disa.remove(-1)
                self.anukunna_disa = self.disa[self.dadi_lekka]
            elif info == 1:
                self.enemy_board[x][y] = 1
            elif info == 2:
                self.akada += 1
                self.enemy_board[x][y] = 0
                self.dadi_rakam = 1
                (self.dabba).append([x, y]) 
                if(y-1<0 or self.enemy_board[x][y-1]!=-1):
                    self.disa.remove(1)
                if(y+1>9 or self.enemy_board[x][y+1]!=-1):
                    self.disa.remove(2)
                if(x-1<0  or self.enemy_board[x-1][y]!=-1):
                    self.disa.remove(-2)
                if(x+1>9 or self.enemy_board[x+1][y]!=-1):
                    self.disa.remove(-1)
                self.anukunna_disa = self.disa[self.dadi_lekka]
            elif info == 3:
                self.akada += 1
                self.enemy_board[x][y] = 0
                self.dadi_rakam = 1
                (self.dabba).append([x, y]) 
                if(y-1<0 or self.enemy_board[x][y-1]!=-1):
                    self.disa.remove(1)
                if(y+1>9 or self.enemy_board[x][y+1]!=-1):
                    self.disa.remove(2)
                if(x-1<0  or self.enemy_board[x-1][y]!=-1):
                    self.disa.remove(-2)
                if(x+1>9 or self.enemy_board[x+1][y]!=-1):
                    self.disa.remove(-1)
                self.anukunna_disa = self.disa[self.dadi_lekka]
                #hawkeye on
                self.hawkeye = 1
        elif self.dadi_rakam == 1:
            if self.dega_kannu == 1:
                self.akada += 1
                self.dega_kannu = 0
                if info == 0:
                    self.enemy_board[x][y] = 0
                    self.dadi_rakam = 2
                    self.anukunna_disa = self.disa[self.dadi_lekka]
                else:
                    self.dadi_rakam = 2
                    self.enemy_board[x][y] = 1
                    self.anukunna_disa = self.disa[self.dadi_lekka]
            elif info == 0:
                self.akada += 1
                self.enemy_board[x][y] = 0
                self.dadi_rakam = 2
                (self.dabba).append([x,y])
                self.anukunna_disa = self.disa[self.dadi_lekka]
                move = self.anukunna_disa
                x1 = -1
                y1 = -1
                if(move==2 and self.dabba[-1][1]+1<=9 and self.enemy_board[self.dabba[-1][0]][self.dabba[-1][1]+1]==-1):
                    x1 = self.dabba[-1][0]
                    y1 = self.dabba[-1][1]+1
                elif(move==1 and self.dabba[-1][1]-1>=0 and self.enemy_board[self.dabba[-1][0]][self.dabba[-1][1]-1]==-1):
                    x1 = self.dabba[-1][0]
                    y1 = self.dabba[-1][1]-1
                elif(move==-2 and self.dabba[-1][0]-1>=0 and self.enemy_board[self.dabba[-1][0]-1][self.dabba[-1][1]]==-1):
                    x1 = self.dabba[-1][0]-1
                    y1 = self.dabba[-1][1]
                elif(move==-1 and self.dabba[-1][0]+1<=9 and self.enemy_board[self.dabba[-1][0]+1][self.dabba[-1][1]]==-1):
                    x1 = self.dabba[-1][0]+1
                    y1 = self.dabba[-1][1]
                if x1 == -1 and y1 == -1:
                    #next search point impossible
                    fix = False
                    self.dadi_sthiti = 1
                    pivot = self.dabba[0]
                    self.dabba = [pivot]
                    if(self.anukunna_disa==1):
                        if(2 in self.disa):
                            self.anukunna_disa = 2
                            fix = True
                    elif(self.anukunna_disa==2):
                        if(1 in self.disa):
                            self.anukunna_disa = 1
                            fix = True
                    elif(self.anukunna_disa==-2):
                        if(-1 in self.disa):
                            self.anukunna_disa = -1
                            fix = True
                    elif(self.anukunna_disa==-1):
                        if(-2 in self.disa):
                            self.anukunna_disa = -2
                            fix = True

                    if(not fix):
                        self.dadi_rakam = 0
                        self.dabba = []
                        self.dadi_lekka = 0
                        self.anukunna_disa = 0
                        self.dadi_sthiti = 0
                        self.disa = [2, -2, 1, -1]
            elif info == 1:
                self.enemy_board[x][y] = 1
                if self.dadi_lekka < len(self.disa)-1:
                    self.dadi_lekka+=1
                    self.anukunna_disa = self.disa[self.dadi_lekka]
                else:
                    self.dadi_rakam = 0
                    self.dabba = []
                    self.dadi_lekka = 0
                    self.anukunna_disa = 0
                    self.dadi_sthiti = 0
                    self.disa = [2, -2, 1, -1]
            elif info == 2:
                self.akada += 1
                self.enemy_board[x][y] = 0
                self.dadi_rakam = 2
                (self.dabba).append([x,y])
                self.anukunna_disa = self.disa[self.dadi_lekka]
                move = self.anukunna_disa
                x1 = -1
                y1 = -1
                if(move==2 and self.dabba[-1][1]+1<=9 and self.enemy_board[self.dabba[-1][0]][self.dabba[-1][1]+1]==-1):
                    x1 = self.dabba[-1][0]
                    y1 = self.dabba[-1][1]+1
                elif(move==1 and self.dabba[-1][1]-1>=0 and self.enemy_board[self.dabba[-1][0]][self.dabba[-1][1]-1]==-1):
                    x1 = self.dabba[-1][0]
                    y1 = self.dabba[-1][1]-1
                elif(move==-2 and self.dabba[-1][0]-1>=0 and self.enemy_board[self.dabba[-1][0]-1][self.dabba[-1][1]]==-1):
                    x1 = self.dabba[-1][0]-1
                    y1 = self.dabba[-1][1]
                elif(move==-1 and self.dabba[-1][0]+1<=9 and self.enemy_board[self.dabba[-1][0]+1][self.dabba[-1][1]]==-1):
                    x1 = self.dabba[-1][0]+1
                    y1 = self.dabba[-1][1]
                if x1 == -1 and y1 == -1:
                    fix = False
                    self.dadi_sthiti = 1
                    pivot = self.dabba[0]
                    self.dabba = [pivot]
                    if(self.anukunna_disa==1):
                        if(2 in self.disa):
                            self.anukunna_disa = 2
                            fix = True
                    elif(self.anukunna_disa==2):
                        if(1 in self.disa):
                            self.anukunna_disa = 1
                            fix = True
                    elif(self.anukunna_disa==-2):
                        if(-1 in self.disa):
                            self.anukunna_disa = -1
                            fix = True
                    elif(self.anukunna_disa==-1):
                        if(-2 in self.disa):
                            self.anukunna_disa = -2
                            fix = True

                    if(not fix):
                        if self.akada in self.migilipoina_ships:
                            self.migilipoina_ships.remove(self.akada)
                        self.akada = 0
                        self.dadi_rakam = 0
                        self.dabba = []
                        self.dadi_lekka = 0
                        self.anukunna_disa = 0
                        self.dadi_sthiti = 0
                        self.disa = [2, -2, 1, -1]
            elif info == 3:
                self.akada += 1
                self.enemy_board[x][y] = 0
                self.dadi_rakam = 2
                (self.dabba).append([x,y])
                self.dega_kannu = 1
                self.anukunna_disa = self.disa[self.dadi_lekka]
                move = self.anukunna_disa
                x1 = -1
                y1 = -1
                if(move==2 and self.dabba[-1][1]+1<=9 and self.enemy_board[self.dabba[-1][0]][self.dabba[-1][1]+1]==-1):
                    x1 = self.dabba[-1][0]
                    y1 = self.dabba[-1][1]+1
                elif(move==1 and self.dabba[-1][1]-1>=0 and self.enemy_board[self.dabba[-1][0]][self.dabba[-1][1]-1]==-1):
                    x1 = self.dabba[-1][0]
                    y1 = self.dabba[-1][1]-1
                elif(move==-2 and self.dabba[-1][0]-1>=0 and self.enemy_board[self.dabba[-1][0]-1][self.dabba[-1][1]]==-1):
                    x1 = self.dabba[-1][0]-1
                    y1 = self.dabba[-1][1]
                elif(move==-1 and self.dabba[-1][0]+1<=9 and self.enemy_board[self.dabba[-1][0]+1][self.dabba[-1][1]]==-1):
                    x1 = self.dabba[-1][0]+1
                    y1 = self.dabba[-1][1]
                if x1 == -1 and y1 == -1:
                    fix = False
                    self.dadi_sthiti = 1
                    pivot = self.dabba[0]
                    self.dabba = [pivot]
                    if(self.anukunna_disa==1):
                        if(2 in self.disa):
                            self.anukunna_disa = 2
                            fix = True
                    elif(self.anukunna_disa==2):
                        if(1 in self.disa):
                            self.anukunna_disa = 1
                            fix = True
                    elif(self.anukunna_disa==-2):
                        if(-1 in self.disa):
                            self.anukunna_disa = -1
                            fix = True
                    elif(self.anukunna_disa==-1):
                        if(-2 in self.disa):
                            self.anukunna_disa = -2
                            fix = True

                    if(not fix):
                        if self.akada in self.migilipoina_ships:
                            self.migilipoina_ships.remove(self.akada)
                        self.akada = 0
                        self.dadi_rakam = 0
                        self.dabba = []
                        self.dadi_lekka = 0
                        self.anukunna_disa = 0
                        self.dadi_sthiti = 0
                        self.disa = [2, -2, 1, -1]
        elif self.dadi_rakam == 2:
            if self.dega_kannu == 1:
                self.akada += 1
                self.dega_kannu = 0
                move = self.anukunna_disa
                x1 = -1
                y1 = -1
                if(move==2 and self.dabba[-1][1]+1<=9 and self.enemy_board[self.dabba[-1][0]][self.dabba[-1][1]+1]==-1):
                    x1 = self.dabba[-1][0]
                    y1 = self.dabba[-1][1]+1
                elif(move==1 and self.dabba[-1][1]-1>=0 and self.enemy_board[self.dabba[-1][0]][self.dabba[-1][1]-1]==-1):
                    x1 = self.dabba[-1][0]
                    y1 = self.dabba[-1][1]-1
                elif(move==-2 and self.dabba[-1][0]-1>=0 and self.enemy_board[self.dabba[-1][0]-1][self.dabba[-1][1]]==-1):
                    x1 = self.dabba[-1][0]-1
                    y1 = self.dabba[-1][1]
                elif(move==-1 and self.dabba[-1][0]+1<=9 and self.enemy_board[self.dabba[-1][0]+1][self.dabba[-1][1]]==-1):
                    x1 = self.dabba[-1][0]+1
                    y1 = self.dabba[-1][1]
                if x1 == -1 and y1 == -1:
                    if(self.dadi_sthiti==0):
                        fix = False
                        self.dadi_sthiti = 1
                        pivot = self.dabba[0]
                        self.dabba = [pivot]
                        if(self.anukunna_disa==1):
                            if(2 in self.disa):
                                self.anukunna_disa = 2
                                fix = True
                        elif(self.anukunna_disa==2):
                            if(1 in self.disa):
                                self.anukunna_disa = 1
                                fix = True
                        elif(self.anukunna_disa==-2):
                            if(-1 in self.disa):
                                self.anukunna_disa = -1
                                fix = True
                        elif(self.anukunna_disa==-1):
                            if(-2 in self.disa):
                                self.anukunna_disa = -2
                                fix = True
                        if(not fix):
                            if self.akada in self.migilipoina_ships:
                                self.migilipoina_ships.remove(self.akada)
                            self.akada = 0
                            self.dadi_rakam = 0
                            self.dabba = []
                            self.dadi_lekka = 0
                            self.anukunna_disa = 0
                            self.dadi_sthiti = 0
                            self.disa = [2, -2, 1, -1]

                    elif(self.dadi_sthiti == 1):
                        if self.akada in self.migilipoina_ships:
                            self.migilipoina_ships.remove(self.akada)
                        self.akada = 0
                        self.dadi_rakam = 0 
                        self.dabba = []
                        self.dadi_lekka = 0
                        self.anukunna_disa = 0
                        self.dadi_sthiti = 0
                        self.disa = [2, -2, 1, -1]
                if info == 0:
                    self.enemy_board[x][y] = 0
                    self.anukunna_disa = self.disa[self.dadi_lekka]
                else:
                    self.enemy_board[x][y] = 1
                    self.anukunna_disa = self.disa[self.dadi_lekka]
            elif info == 0:
                self.akada += 1
                self.enemy_board[x][y] = 0
                (self.dabba).append([x,y])
                move = self.anukunna_disa
                x1 = -1
                y1 = -1
                if(move==2 and self.dabba[-1][1]+1<=9 and self.enemy_board[self.dabba[-1][0]][self.dabba[-1][1]+1]==-1):
                    x1 = self.dabba[-1][0]
                    y1 = self.dabba[-1][1]+1
                elif(move==1 and self.dabba[-1][1]-1>=0 and self.enemy_board[self.dabba[-1][0]][self.dabba[-1][1]-1]==-1):
                    x1 = self.dabba[-1][0]
                    y1 = self.dabba[-1][1]-1
                elif(move==-2 and self.dabba[-1][0]-1>=0 and self.enemy_board[self.dabba[-1][0]-1][self.dabba[-1][1]]==-1):
                    x1 = self.dabba[-1][0]-1
                    y1 = self.dabba[-1][1]
                elif(move==-1 and self.dabba[-1][0]+1<=9 and self.enemy_board[self.dabba[-1][0]+1][self.dabba[-1][1]]==-1):
                    x1 = self.dabba[-1][0]+1
                    y1 = self.dabba[-1][1]
                if x1 == -1 and y1 == -1:
                    if(self.dadi_sthiti==0):
                        fix = False
                        self.dadi_sthiti = 1
                        pivot = self.dabba[0]
                        self.dabba = [pivot]
                        if(self.anukunna_disa==1):
                            if(2 in self.disa):
                                self.anukunna_disa = 2
                                fix = True
                        elif(self.anukunna_disa==2):
                            if(1 in self.disa):
                                self.anukunna_disa = 1
                                fix = True
                        elif(self.anukunna_disa==-2):
                            if(-1 in self.disa):
                                self.anukunna_disa = -1
                                fix = True
                        elif(self.anukunna_disa==-1):
                            if(-2 in self.disa):
                                self.anukunna_disa = -2
                                fix = True
                        if(not fix):
                            self.dadi_rakam = 0
                            self.dabba = []
                            self.dadi_lekka = 0
                            self.anukunna_disa = 0
                            self.dadi_sthiti = 0
                            self.disa = [2, -2, 1, -1]

                    elif(self.dadi_sthiti == 1):
                        self.dadi_rakam = 0 
                        self.dabba = []
                        self.dadi_lekka = 0
                        self.anukunna_disa = 0
                        self.dadi_sthiti = 0
                        self.disa = [2, -2, 1, -1]
            elif info == 1:
                self.enemy_board[x][y] = 1
                if(self.dadi_sthiti==0):
                    fix = False
                    self.dadi_sthiti = 1
                    pivot = self.dabba[0]
                    self.dabba = [pivot]
                    if(self.anukunna_disa==1):
                        if(2 in self.disa):
                            self.anukunna_disa = 2
                            fix = True
                    elif(self.anukunna_disa==2):
                        if(1 in self.disa):
                            self.anukunna_disa = 1
                            fix = True
                    elif(self.anukunna_disa==-2):
                        if(-1 in self.disa):
                            self.anukunna_disa = -1
                            fix = True
                    elif(self.anukunna_disa==-1):
                        if(-2 in self.disa):
                            self.anukunna_disa = -2
                            fix = True

                    if(not fix):
                        self.dadi_rakam = 0
                        self.dabba = []
                        self.dadi_lekka = 0
                        self.anukunna_disa = 0
                        self.dadi_sthiti = 0
                        self.disa = [2, -2, 1, -1]

                elif(self.dadi_sthiti == 1):
                    self.dadi_rakam = 0 
                    self.dabba = []
                    self.dadi_lekka = 0
                    self.anukunna_disa = 0
                    self.dadi_sthiti = 0
                    self.disa = [2, -2, 1, -1]
            elif info == 2:
                self.akada += 1
                self.enemy_board[x][y] = 0
                (self.dabba).append([x,y])
                move = self.anukunna_disa
                x1 = -1
                y1 = -1
                if(move==2 and self.dabba[-1][1]+1<=9 and self.enemy_board[self.dabba[-1][0]][self.dabba[-1][1]+1]==-1):
                    x1 = self.dabba[-1][0]
                    y1 = self.dabba[-1][1]+1
                elif(move==1 and self.dabba[-1][1]-1>=0 and self.enemy_board[self.dabba[-1][0]][self.dabba[-1][1]-1]==-1):
                    x1 = self.dabba[-1][0]
                    y1 = self.dabba[-1][1]-1
                elif(move==-2 and self.dabba[-1][0]-1>=0 and self.enemy_board[self.dabba[-1][0]-1][self.dabba[-1][1]]==-1):
                    x1 = self.dabba[-1][0]-1
                    y1 = self.dabba[-1][1]
                elif(move==-1 and self.dabba[-1][0]+1<=9 and self.enemy_board[self.dabba[-1][0]+1][self.dabba[-1][1]]==-1):
                    x1 = self.dabba[-1][0]+1
                    y1 = self.dabba[-1][1]
                if x1 == -1 and y1 == -1:
                    if(self.dadi_sthiti==0):
                        fix = False
                        self.dadi_sthiti = 1
                        pivot = self.dabba[0]
                        self.dabba = [pivot]
                        if(self.anukunna_disa==1):
                            if(2 in self.disa):
                                self.anukunna_disa = 2
                                fix = True
                        elif(self.anukunna_disa==2):
                            if(1 in self.disa):
                                self.anukunna_disa = 1
                                fix = True
                        elif(self.anukunna_disa==-2):
                            if(-1 in self.disa):
                                self.anukunna_disa = -1
                                fix = True
                        elif(self.anukunna_disa==-1):
                            if(-2 in self.disa):
                                self.anukunna_disa = -2
                                fix = True
                        if(not fix):
                            if self.akada in self.migilipoina_ships:
                                self.migilipoina_ships.remove(self.akada)
                            self.akada = 0
                            self.dadi_rakam = 0
                            self.dabba = []
                            self.dadi_lekka = 0
                            self.anukunna_disa = 0
                            self.dadi_sthiti = 0
                            self.disa = [2, -2, 1, -1]

                    elif(self.dadi_sthiti == 1):
                        if self.akada in self.migilipoina_ships:
                            self.migilipoina_ships.remove(self.akada)
                        self.akada = 0
                        self.dadi_rakam = 0 
                        self.dabba = []
                        self.dadi_lekka = 0
                        self.anukunna_disa = 0
                        self.dadi_sthiti = 0
                        self.disa = [2, -2, 1, -1]
            elif info == 3:
                self.akada += 1
                self.enemy_board[x][y] = 0
                (self.dabba).append([x,y])
                self.dega_kannu = 1
                move = self.anukunna_disa
                x1 = -1
                y1 = -1
                if(move==2 and self.dabba[-1][1]+1<=9 and self.enemy_board[self.dabba[-1][0]][self.dabba[-1][1]+1]==-1):
                    x1 = self.dabba[-1][0]
                    y1 = self.dabba[-1][1]+1
                elif(move==1 and self.dabba[-1][1]-1>=0 and self.enemy_board[self.dabba[-1][0]][self.dabba[-1][1]-1]==-1):
                    x1 = self.dabba[-1][0]
                    y1 = self.dabba[-1][1]-1
                elif(move==-2 and self.dabba[-1][0]-1>=0 and self.enemy_board[self.dabba[-1][0]-1][self.dabba[-1][1]]==-1):
                    x1 = self.dabba[-1][0]-1
                    y1 = self.dabba[-1][1]
                elif(move==-1 and self.dabba[-1][0]+1<=9 and self.enemy_board[self.dabba[-1][0]+1][self.dabba[-1][1]]==-1):
                    x1 = self.dabba[-1][0]+1
                    y1 = self.dabba[-1][1]
                if x1 == -1 and y1 == -1:
                    if(self.dadi_sthiti==0):
                        fix = False
                        self.dadi_sthiti = 1
                        pivot = self.dabba[0]
                        self.dabba = [pivot]
                        if(self.anukunna_disa==1):
                            if(2 in self.disa):
                                self.anukunna_disa = 2
                                fix = True
                        elif(self.anukunna_disa==2):
                            if(1 in self.disa):
                                self.anukunna_disa = 1
                                fix = True
                        elif(self.anukunna_disa==-2):
                            if(-1 in self.disa):
                                self.anukunna_disa = -1
                                fix = True
                        elif(self.anukunna_disa==-1):
                            if(-2 in self.disa):
                                self.anukunna_disa = -2
                                fix = True
                        if(not fix):
                            if self.akada in self.migilipoina_ships:
                                self.migilipoina_ships.remove(self.akada)
                            self.akada = 0
                            self.dadi_rakam = 0
                            self.dabba = []
                            self.dadi_lekka = 0
                            self.anukunna_disa = 0
                            self.dadi_sthiti = 0
                            self.disa = [2, -2, 1, -1]

                    elif(self.dadi_sthiti == 1):
                        if self.akada in self.migilipoina_ships:
                            self.migilipoina_ships.remove(self.akada)
                        self.akada = 0
                        self.dadi_rakam = 0 
                        self.dabba = []
                        self.dadi_lekka = 0
                        self.anukunna_disa = 0
                        self.dadi_sthiti = 0
                        self.disa = [2, -2, 1, -1]

ships = [
[0 , 0, 3, 0],
[3 ,1 ,5 , 0],
[3 ,9 ,4 ,0],
[8 ,4 ,4 ,1],
[0 , 4 ,5 ,1],]

enemy_board = []
for i in range(10):
    lis = []
    for j in range(10):
        lis.append(-1)
    enemy_board.append(lis)