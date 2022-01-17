from ..BattleGround import main
import random

TEAM_NAME = "EXAMPLE_TEAM_1"

def set_board(): ## Pre-defined function
    board = [
        [0 , 1 , 0, 0],
        [1 , 1 , 0, 1]
    ]

    return board


def attack(): ## pre-defined function
    x = random.randint(0,1)
    y = random.randint(0,3)
    hit_or_miss()
    return (x,y)

def hit_or_miss():
    file_name = str(TEAM_NAME) + ".txt"
    with open(file_name, "r") as file1:
        print(TEAM_NAME + " : " + file1.read())
    pass
