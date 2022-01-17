from itertools import chain
from importlib import import_module
import time

rows = 2
cols = 4

class BattleShip :

    def __init__(self, board, team_name : str, opponent_team_name):
        self.board = board
        self.team_name = team_name
        self.opponent_team_name = opponent_team_name
        self.hit_or_miss = -1
        self.check()


    ## Opponent attacked. Returns True if opponent has hit the player's ship, otherwise return 0
    def got_attacked(self, x : int , y : int) -> bool:
        
        if x > 2 or y > 4 or x < -2 or y < -4:
            self.hit_or_miss = -1
            self.check()
            return "FIRED OUT OF BATTLEZONE"

        if self.board[x][y] == 1:
            self.board[x][y] = 0
            self.hit_or_miss = 1
            self.check()
            return "HIT !!"

        self.hit_or_miss = 0
        self.check()
        return "MISS !!"
    
    def check(self):
        file_name = str(self.opponent_team_name) + ".txt"
        with open(file_name, "w+") as file1:
            file1.write(str(self.hit_or_miss))


    def check_loss(self) -> bool:
        if all(x == 0 for x in chain(*self.board)) : 
            return True

        return False


player = "player"
    
def check():
    return "Yo"

# print((import_module("Battleship.example_submission.team1")).set_board())
TEAM1 = "team1"
TEAM2 = "team2"

team1_module = import_module(f"Battleship.example_submission.{TEAM1}")
team2_module = import_module(f"Battleship.example_submission.{TEAM2}")

team1 = BattleShip(team1_module.set_board(), team_name = team1_module.TEAM_NAME, opponent_team_name = team2_module.TEAM_NAME)
team2 = BattleShip(team2_module.set_board(), team_name = team2_module.TEAM_NAME, opponent_team_name = team1_module.TEAM_NAME)


# x,y = team1_module.attack()

# print((x,y))

# team2.attacked(x, y)

while True:

    x, y = team1_module.attack()
    print("Team 1 attacked at  : " + str((x,y)))
    res = team2.got_attacked(x, y)
    time.sleep(1)
    print(res)
    if team2.check_loss():
        print("Team 1 has won")
        break


    x, y = team2_module.attack()
    print(f"Team 2 attacked at : ({x, y})")
    res = team1.got_attacked(x, y)
    time.sleep(1)
    print(res)
    if team1.check_loss():
        print("Team 2 has won")
        break

     
