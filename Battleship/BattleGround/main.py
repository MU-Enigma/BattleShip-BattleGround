from itertools import chain
import time
from ..utils import RenderTest as animation
from ..example_submission import team1
from ..example_submission import team2


def update_hit(board, x, y):
    info = -1
    if x > len(board) or y > len(board[0]) or x < -(len(board)) or y < -(len(board[0])):
            print("FIRED OUT OF BATTLEZONE")

    elif board[x][y] == 1:
            info = 0
            board[x][y] = info
            print("HIT !!") 
    else:
        print("MISS !!")
        info = 1 ## MISS

    return (board, info)



def game_over(board):
    if all(x == 0 for x in chain(*board)) : 
        return True

    return False


def special_check():
    pass


team1_module = team1.BattleShip()
team2_module = team2.BattleShip()

team1_board = team1_module.set_board()
team2_board = team2_module.set_board()

## For Pygame
animation.board1 = team1_board
animation.board2 = team2_board
animation.initialize()


while True:

    x, y = team1_module.attack()
    print("Team 1 attacked at  : " + str((x,y)))
    team2_board, info = update_hit(team2_board, x, y) ## Updates the board as well as returns hit/miss
    team1_module.hit_or_miss(x, y, info)  ## info = 0 for hit , 1 for miss, and -1 for out of range shooting

    animation.update(team1_board, team2_board)     ## Update Animation board

    time.sleep(1)
    if game_over(team2_board):
        print("Team 1 has won !!!")
        break
    

    x, y = team2_module.attack()
    print("Team 2 attacked at  : " + str((x,y)))
    team1_board, info = update_hit(team1_board, x, y)
    team2_module.hit_or_miss(x, y, info)

    animation.update(team1_board, team2_board)     ## Update Animation board
    
    time.sleep(1)
    if game_over(team1_board):
        print("Team 2 has won !!!")
        break