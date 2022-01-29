import math
import random

import positionCalculators
from animator import animatedValue
import pygame
import os


pygame.init()
pygame.display.init()

#Loading Resources

tilepath1 = "../Assets/1/"
tilepath2 = "../Assets/2/"
OnBoardPath = "../Assets/OnBoard/"

tiles = {}

#Window Control variables
window_size = [1600, 800]
window_caption = "Battleship-BattleGround"
FPS=75
BackgroundColorRGB = [15, 0, 0]  # [15, 250, 190]

# Runtime Variables
running = True
screen = pygame.display.set_mode(window_size)
clock = pygame.time.Clock()


side_column_dimensions = []
leaderboard_dimensions = []
board_elem_dim = []
cell_size = []
cell_size_index = 0
dT = 1

shi1 = []  # Each gun turrent will be stored as [position, rotation]
shi2 = []
bullet = [[-100, -100], 0]  # same format as gun turrent [[position], rotation]

# Control Variables
team1_info = None
team2_info = None
leaderboard_info = None
drawgrid = False

board1 = []
board2 = []
ships1 = []
ships2 = []

onetimecalculations = True
in_animation = False

"""
board nums:
0 - water
1 - ship part
2 - destroyed ship part
"""

# Draw Variables
board_margin = 10
max_board_dim = []
grid_line_color = [192, 192, 192]

side_column_margin = 10
side_column_width = 0
side_column_background_color = [192, 192, 192]

leaderboard_margin = 10
leaderboard_height = 0
leaderboard_background_color = [192, 192, 192]

divider_line_thickness = 5

turrent_cell_size = 45 # good ratio: 400:45 (board size to turrent_cell_size)

cell_colors = [ #Temporarily representing ships as flat colors
    [15, 0, 0],  # water color
    [49, 60, 62],  # Ship-body
    [255, 100, 0],  # destroyed ship
    [255, 0, 89]
]


# Animation Variables


def min(l):
    v = l[0]
    index = 0
    mindex = 0
    for elem in l:
        if elem < v:
            v = elem
            mindex = index
        index+=1
    return mindex

def blitRotateCenter(surf, image, topleft, angle):

    # Got the below code from the internet : https://stackoverflow.com/questions/4183208/how-do-i-rotate-an-image-around-its-center-using-pygame

    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)

    surf.blit(rotated_image, new_rect)

def render_side_column(pos, team_info):
    pygame.draw.rect(screen, side_column_background_color, pygame.Rect(pos[0],
                                                                       pos[1],
                                                                       side_column_dimensions[0],
                                                                       side_column_dimensions[1]))

    #TODO: Write stuff to render/visualize data related to each team (team_info)


def render_leaderboard(pos):
    pygame.draw.rect(screen, leaderboard_background_color, pygame.Rect(pos[0],
                                                                       pos[1],
                                                                       leaderboard_dimensions[0],
                                                                       leaderboard_dimensions[1]))

    #TODO: Write stuff to render/visualize data related to the leaderboard/scoresheet


def nomenclature(board, pos):
    s_tiles = []

    for y in range(3):
        for x in range(3):
            index_x = pos[0]-1+x
            index_y = pos[1]-1+y
            if index_x < 0 or index_y < 0 or index_x > len(board[0])-1 or index_y > len(board)-1:
                s_tiles.append(0)
            else:
                s_tiles.append(board[index_y][index_x])

    # top, left, right, bottom
    return str(s_tiles[1]) + str(s_tiles[3]) + str(s_tiles[5]) + str(s_tiles[7])


def render_board(pos, board, shi):
    index = min(cell_size)

    # Drawing cells
    for x in range(board_elem_dim[0]):
        for y in range(board_elem_dim[1]):
            """pygame.draw.rect(screen, cell_colors[board[y][x]], pygame.Rect(pos[0]+(x * cell_size[index]),
                                                                           pos[1]+(y * cell_size[index]),
                                                                           cell_size[index],
                                                                           cell_size[index]))"""


            cell_pos = [pos[0]+(x * cell_size[index]), pos[1]+(y * cell_size[index])]
            if x != board_elem_dim[0] and y != board_elem_dim[1]:
                if board[y][x] == 1:
                    screen.blit(tiles[nomenclature(board, (x, y))], cell_pos)

            #TODO: draw turrents here.

            for ship in shi:
                blitRotateCenter(screen, tiles['GunTurrent3'], ship[0], ship[1](dT))
                #screen.blit(surf, ship[0])

    # Must shift pos-y, pos-x depending on lesser size.
    # Drawing Grid Lines, can compute and store intersection map for speed gains here.

    if drawgrid:
        for x in range(board_elem_dim[0]):
            if x != 0:
                pygame.draw.line(screen,
                                 grid_line_color,
                                 (pos[0]+(x*cell_size[index]), pos[1]),
                                 (pos[0]+(x*cell_size[index]), pos[1]+(board_elem_dim[1]*cell_size[index])))

        for y in range(board_elem_dim[1]):
            if y != 0:
                pygame.draw.line(screen,
                                 grid_line_color,
                                 (pos[0], pos[1]+(y*cell_size[index])),
                                 (pos[0]+(board_elem_dim[0]*cell_size[index]), pos[1]+(y*cell_size[index])))

    # Drawing bullet
    blitRotateCenter(screen, tiles['bullet'], bullet[0], bullet[1])


def render():
    """
    Draw Plan:
    Left Column: Team 1 info
    Left Board: Team 1 board
    Middle Line: Board Division Line (makes stuff look neat)
    Right Column: Team 2 info
    Right Board Team 2 Board
    Bottom Row box: Leaderboard and other statistics.

    """

    screen.fill(BackgroundColorRGB)

    """
    1]Can calculate these positions in the initialize() 
    for speed gains, but I'm not patient enough to change all this.
    2]Can pass surfaces through antialias function to polish render.
    """

    # Drawing Side-info columns
    render_side_column([side_column_margin, side_column_margin], "team-info")
    render_side_column([window_size[0]-(side_column_margin+side_column_width),
                        side_column_margin], "team-info")
    render_leaderboard([leaderboard_margin, window_size[1]-(leaderboard_height+leaderboard_margin)])

    render_board([side_column_width+(side_column_margin*2)+board_margin,
                  board_margin], board1, shi1)

    render_board([window_size[0]-(side_column_width+(side_column_margin*2)+board_margin+max_board_dim[0]),
                  board_margin], board2, shi2)

def load_tiles(tilepath):
    for name in os.listdir(tilepath):
        tiles[os.path.splitext(name)[0]] = pygame.image.load(tilepath+str(name))

def initialize():
    # Only run after updating above variables to your preferences.

    global screen, window_size, side_column_dimensions, leaderboard_dimensions, board_elem_dim, cell_size, tiles, turrent_cell_size, cell_size_index

    assert len(board1) == len(board2)
    assert len(board1[0]) == len(board2[0])

    #TODO: Add assertions here to ensure non-negative dimension values

    # Doing some prelimanary calculations here
    board_elem_dim = [len(board1[0]), len(board1)]
    cell_size = [max_board_dim[0] / board_elem_dim[0],
                 max_board_dim[1] / board_elem_dim[1]]

    index = min(cell_size)
    cell_size_index = index

    # RecalculateWindowSizeHere
    width = int((side_column_margin*4) + (board_margin*4) + divider_line_thickness + (side_column_width*2) + (max_board_dim[0]*2))

    if side_column_margin > board_margin:
        gmargin = side_column_margin
    else:
        gmargin = board_margin

    height = int((leaderboard_margin*2) + leaderboard_height + (len(board1)*cell_size[index]) + gmargin)

    window_size = [width, height]
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption(window_caption)

    # Calculate runtime constants (draw stuff)

    side_column_dimensions = [side_column_width,
                              height-(leaderboard_height+(leaderboard_margin*2)+(side_column_margin*2))]

    leaderboard_dimensions = [width-(leaderboard_margin*2), leaderboard_height]



    assert turrent_cell_size < cell_size[index]  # Ensuring turrents are smaller than ship size.

    # Loading tiles
    load_tiles(tilepath1)
    load_tiles(tilepath2)

    # Resize imported tiles
    for key in tiles.keys():
        tiles[key] = pygame.transform.scale(tiles[key], [int(cell_size[index]), int(cell_size[index])])

    # Loading Guns
    load_tiles(OnBoardPath)
    if index == 0:
        boardsize = len(board1[0])
    else:
        boardsize = len(board1)
    turrent_cell_size = int(boardsize*cell_size[index]/400)*45

    # Resizing Guns
    tiles['GunTurrent3'] = pygame.transform.scale(tiles['GunTurrent3'], (turrent_cell_size, turrent_cell_size))
    tiles['bullet'] = pygame.transform.scale(tiles['bullet'], (turrent_cell_size, turrent_cell_size))

    # Calculating Turrent Positions
    # center of turrents will be at the center of ships.
    shipos1 = positionCalculators.calculateShipPositions(ships1, cell_size[index], [side_column_width+(side_column_margin*2)+board_margin, board_margin], turrent_cell_size)
    shipos2 = positionCalculators.calculateShipPositions(ships2, cell_size[index], [window_size[0]-(side_column_width+(side_column_margin*2)+board_margin+max_board_dim[0]), board_margin], turrent_cell_size)

    for shipos in shipos1:
        shi1.append([shipos, animatedValue(0, FPS)])

    for shipos in shipos2:
        shi2.append([shipos, animatedValue(180, FPS)])

#Everything below is cheap AF (probably have to rewrite all the animation shit)

"""
Animation will be implemented in the following manner:
    1] Bullet Positions
    2] Screen Shake values (relevant vars)
    3] Light shock values (screen exposure)
    4] Bullet position, rotation

will act persistantly during the render process of the screen.
The final output screen can be animated by sequenctially and systematically changing these variables.

    
"""


def animation_handler(anim_instruction):
    global screen, running, clock, count, dT
    dT = clock.tick(FPS) / 1000
    while in_animation:
        render()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()
        dT = clock.tick(FPS)/1000

def draw_call(animation_instruction):
    global screen, running, clock, count, in_animation
    #animation_instruction is of the following format: [animation_id, animation_info]
    if animation_instruction[0] != None:
        in_animation = True
        animation_handler(animation_instruction)
    render()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
    clock.tick(FPS)



