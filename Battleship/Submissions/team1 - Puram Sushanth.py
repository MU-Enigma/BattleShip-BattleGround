import random
class BattleShip:
    def __init__(self):
        self.team_name = "CRIP"
        self.ships = ships
        self.opponent_board = opponent_board
        self.info = -1

    def set_ships(self):
        return self.ships
    
    global a #for traversing the attack_pos array
    a = -1
    global temp #for attacking in +ve x-axis
    global counter #for attacking
    global temp2 #for attacking in -ve x-axis
    global temp4 #for attacking in -ve y-axis
    global temp3 #for attacking in +ve y-axis
    global board #enemy's board
    global temp5 #for hawkeye
    global check #for a <= 33
    board = [
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
    #intiating
    temp2 = 0
    temp3 = 0
    temp4 = 0
    temp5 = 0
    temp = 0
    check = 0
    counter = 0
    def attack(self):
        #calling variable in the function
        global a
        global temp
        global counter
        global board
        global temp2
        global temp3
        global temp4
        global temp5
        global clear
        global check
        attack_pos = [[0,0], [0,3], [0,6], [0,9],
                    [3,0], [6,0], [9,0],
                    [1,1], [4,1], [7,1],
                    [1,4], [1,7],
                    [2,2], [2,5], [2,8],
                    [5,2], [8,2],
                    [3,3], [6,3], [9,3],
                    [3,6], [3,9],
                    [4,4], [4,7],
                    [7,4],
                    [5,5], [8,5],
                    [5,8],
                    [6,6], [6,9],
                    [9,6],
                    [7,7],
                    [8,8],
                    [9,9]]
        if((self.info in [0,2,3]) and temp2 == 0 and temp == 0 and temp3 == 0 and temp4 == 0):
            temp = 1
        if(temp == 1 and temp2 == 0 and temp3 == 0 and temp4 == 0 and check == 0):
            if(attack_pos[a][1] + counter == 9 or self.info == 1):
                counter = 4
                self.info = 0
            if(counter <= 3):
                while board[attack_pos[a][0]][attack_pos[a][1] + counter] == 0 and counter <= 3 and attack_pos[a][1] + counter != 9:
                    counter += 1
                board[attack_pos[a][0]][attack_pos[a][1] + counter] = 0
                if(self.info == 3):
                    for i in range(0,10):
                        board[attack_pos[a][0]][i] = 0
                        board[i][attack_pos[a][1] + counter] = 0
                return (attack_pos[a][0], attack_pos[a][1] + counter)
            else:
                counter = 0
                temp = 0
                temp2 = 1
        if(temp2 == 1 and temp == 0 and temp3 == 0 and temp4 == 0 and check == 0):
            if(attack_pos[a][1] - counter == 0 or self.info == 1):
                counter = 4
                self.info = 0
            if(counter <= 3):
                while board[attack_pos[a][0]][attack_pos[a][1] - counter] == 0 and counter <= 3 and attack_pos[a][1] - counter != 0:
                    counter += 1
                board[attack_pos[a][0]][attack_pos[a][1] - counter] = 0
                if(self.info == 3):
                    for i in range(0,10):
                        board[attack_pos[a][0]][i] = 0
                        board[i][attack_pos[a][1] - counter] = 0
                return (attack_pos[a][0], attack_pos[a][1] - counter)
            else:
                counter = 0
                temp2 = 0
                temp3 = 1
        if(temp3 == 1 and temp == 0 and temp2 == 0 and temp4 == 0 and check == 0):
            if(attack_pos[a][0] + counter == 9 or self.info == 1):
                counter = 4
                self.info = 0
            if(counter <= 3):
                while board[attack_pos[a][0] + counter][attack_pos[a][1]] == 0 and counter <= 3 and attack_pos[a][0] + counter != 9:
                    counter += 1
                board[attack_pos[a][0] + counter][attack_pos[a][1]] = 0
                if(self.info == 3):
                    for i in range(0,10):
                        board[attack_pos[a][0] + counter][i] = 0
                        board[i][attack_pos[a][1]] = 0
                return (attack_pos[a][0] + counter, attack_pos[a][1])
            else:
                counter = 0
                temp3 = 0
                temp4 = 1
        if(temp4 == 1 and temp == 0 and temp3 == 0 and temp2 == 0 and check == 0):
            if(attack_pos[a][0] - counter == 0 or self.info == 1):
                counter = 4
                self.info = 0
            if(counter <= 3):
                while board[attack_pos[a][0] - counter][attack_pos[a][1]] == 0 and counter <= 3 and attack_pos[a][0] - counter != 0:
                    counter += 1
                board[attack_pos[a][0] - counter][attack_pos[a][1]] = 0
                if(self.info == 3):
                    for i in range(0,10):
                        board[attack_pos[a][0] - counter][i] = 0
                        board[i][attack_pos[a][1]] = 0
                        temp5 = 0
                return (attack_pos[a][0] - counter, attack_pos[a][1])
            else:
                counter = 0
                temp4 = 0
        a += 1
        if(check == 1):
            for i in range (0,10):
                for j in range (0,10):
                    if(board[i][j] == -1):
                        board[i][j] = 0
                        return (i,j)
        while board[attack_pos[a][0]][attack_pos[a][1]] == 0 and check == 0:
            if(a < 33):
                a += 1
            if(a == 33):
                check = 1
                break
        board[attack_pos[a][0]][attack_pos[a][1]] = 0
        if(self.info == 3):
            for i in range(0,10):
                board[attack_pos[a][0]][i] = 0
                board[i][attack_pos[a][1]] = 0
        return (attack_pos[a][0], attack_pos[a][1])

    def hit_or_miss(self, x, y, info):
        self.info = info
        # print(self.info)
        # info = 1 for miss, 0 for a hit, -1 for an out of range shooting, 2 for special move nullify. 3 for your next move to be a Hawkeye Shot
        if info != -1 and info == 0:
            self.opponent_board[x][y] = info


ships = [
        [1,3,5,1],
        [3,8,5,0],
        [2,6,4,0],
        [9,4,4,1],
        [6,4,3,1]
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
