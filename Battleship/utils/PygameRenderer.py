import math
import random
import time

import positionCalculators
from animator import AnimatedValue, AnimationStateMachine
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
bullets = []  # same format as gun turrent [[position], rotation]
bullet2 = []
bullet_image = None
bullet2_image = None

# Control Variables
team1_info = None
team2_info = None
leaderboard_info = None
drawgrid = True

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
bullet_velocity = 0.5
bullet1over = False


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

    screen.blit(tiles['1square'], pos)

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
                blitRotateCenter(screen, tiles['GunTurrent2'], ship[0], ship[1](dT))
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

    screen.blit(bullet_image, [bullets[0](), bullets[1]()])
    screen.blit(bullet2_image, [bullet2[0](), bullet2[1]()])

    font = pygame.font.SysFont("Segoe UI", 80)
    img = font.render('Team-I', True, BackgroundColorRGB)
    img = pygame.transform.rotate(img, 90)
    screen.blit(img, (side_column_margin, side_column_dimensions[1]-500))

    font = pygame.font.SysFont("Segoe UI", 80)
    img = font.render('Team-II', True, BackgroundColorRGB)
    img = pygame.transform.rotate(img, 270)
    screen.blit(img, (window_size[0]-side_column_margin-100, side_column_dimensions[1] - 500))

def load_tiles(tilepath):
    for name in os.listdir(tilepath):
        tiles[os.path.splitext(name)[0]] = pygame.image.load(tilepath+str(name))

def initialize():
    # Only run after updating above variables to your preferences.

    global screen, window_size, side_column_dimensions, leaderboard_dimensions, board_elem_dim, cell_size, tiles, turrent_cell_size, cell_size_index, bullets, bullet_image, bullet2, bullet2_image

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
    load_tiles("../Assets/Backgrounds/")

    # Resize imported tiles
    for key in tiles.keys():
        tiles[key] = pygame.transform.scale(tiles[key], [int(cell_size[index]), int(cell_size[index])])

    # Loading Guns
    load_tiles(OnBoardPath)
    if index == 0:
        boardsize = len(board1[0])
    else:
        boardsize = len(board1)
    turrent_cell_size = int(boardsize*cell_size[index]/400)*35

    # Resizing Guns
    tiles['GunTurrent2'] = pygame.transform.scale(tiles['GunTurrent2'], (turrent_cell_size, turrent_cell_size))
    tiles['bullet'] = pygame.transform.scale(tiles['bullet'], (turrent_cell_size, turrent_cell_size))
    tiles['1square'] = pygame.transform.scale(tiles['1square'], (800, 800))

    # Calculating Turrent Positions
    # center of turrents will be at the center of ships.
    shipos1 = positionCalculators.calculateShipPositions(ships1, cell_size[index], [side_column_width+(side_column_margin*2)+board_margin, board_margin], turrent_cell_size)
    shipos2 = positionCalculators.calculateShipPositions(ships2, cell_size[index], [window_size[0]-(side_column_width+(side_column_margin*2)+board_margin+max_board_dim[0]), board_margin], turrent_cell_size)

    for shipos in shipos1:
        shi1.append([shipos, AnimatedValue(0, FPS)])

    for shipos in shipos2:
        shi2.append([shipos, AnimatedValue(180, FPS)])

    board1_pos = [side_column_width + (side_column_margin * 2) + board_margin, board_margin]

    bullets = [AnimatedValue(-turrent_cell_size/2, FPS), AnimatedValue((height/2)-(turrent_cell_size/2), FPS)]
    bullet2 = [AnimatedValue(width+turrent_cell_size/2, FPS), AnimatedValue((height/2)-(turrent_cell_size/2), FPS)]
    bullet_image = tiles['bulletN']
    bullet2_image = tiles['BulletN2']


    #temporary animation blit


# Everything below is cheap AF (probably have to rewrite all the animation shit)


"""

Animation will be implemented in the following manner:
    1] Bullet Positions
    2] Screen Shake values (relevant vars)
    3] Light shock values (screen exposure)
    4] Bullet position, rotation

will act persistantly during the render process of the screen.
The final output screen can be animated by sequenctially and systematically changing these variables.

    
"""

# ---------------------------------------Strike Animation Stuff--------------------------------------------------------

def install_bullet():
    pass

def generateStrikeStateMachine(anim):
    """
    The strike will have the following states with the following animated values:
        1]State 1:
            1] Rotate the turrent:
                1] turrent rotation
        2]State 2: (termination function)
            1] Put the bullet with appropriate rotation in the turrent:
                1] bullet rotation
                1] bullet position
        3]State 3:
            1] Launch the bullet, 2 things will be animated:
                1] Bullet position -> target position
                2] Bullet size (to emulate height)
        4]State 4:
            1] Screen Rumble
            2] Exposure increases(becomes blinding)
        5]State 5: (termination function)
            1] update corresponding board
            2] Reset bullet
        6]State 6:
            1] Screen Rumble
            2] Exposure decreases(becomes imperceptible)




    #turrent_no = random.randint(0, len(shi1)-1)


    board1_pos = [side_column_width+(side_column_margin*2)+board_margin, board_margin]
    board2_pos = [window_size[0]-(side_column_width+(side_column_margin*2)+board_margin+max_board_dim[0]), board_margin]

    states = [
        [
            [[bullets[0][0], board2_pos[0]+cell_size[cell_size_index]*3, bullet_velocity],
            [bullets[0][1], board2_pos[1]+cell_size[cell_size_index]*2, bullet_velocity]],
            []
        ]
    ]


    machine = AnimationStateMachine(states)

    return machine

"""
# ---------------------------------------------------------------------------------------------------------------------

def animation_handler(anim_instruction):
    global screen, running, clock, count, dT,in_animation
    dT = clock.tick(FPS) / 1000


    while in_animation:
        render()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()
        dT = clock.tick(FPS)/1000

frames = 0
shoot = True
setzero = False

def draw_call(animation_instruction):
    global screen, running, clock, count, in_animation, bullet_image, frames, board2, bullet1over, shoot, setzero, bullet2_image
    #animation_instruction is of the following format: [animation_id, animation_info]
    #if animation_instruction[0] != None:
    #    in_animation = True
    #    animation_handler(animation_instruction)

    bullet1over = False
    preframes = 0

    board1_pos = [side_column_width + (side_column_margin * 2) + board_margin, board_margin]
    board2_pos = [window_size[0] - (side_column_width + (side_column_margin * 2) + board_margin + max_board_dim[0]),
                  board_margin]

    bullets[0].animate(board2_pos[0]+cell_size[cell_size_index]*3, bullet_velocity)
    bullets[1].animate(board2_pos[1]+cell_size[cell_size_index]*1, bullet_velocity)


    while True:
        render()
        if preframes > 100:
            if not bullet1over:
                if not bullets[0].animated and not bullets[1].animated:
                    bullet_image = tiles['Explosion']
                    bullet1over = True
                    """
                    if frames > 0 and frames < FPS*0.5*dT:
                        bullet_image = tiles['Explosion']
                    elif frames > FPS*0.5*dT and frames < FPS*0.525*dT:
                        bullet_image = tiles['ExplosionLarge']
                    else:
                        bullet_image = tiles['0010B']
                        bullet1over = True
                        #board2[1][3] = 0"""


            if bullet1over:
                if shoot:
                    bullet2[0].animate(board1_pos[0]+cell_size[cell_size_index]*6, bullet_velocity)
                    bullet2[1].animate(board1_pos[1]+cell_size[cell_size_index]*8, bullet_velocity)
                    shoot = False
                else:
                    if not bullet2[0].animated and not bullet2[1].animated and not setzero:
                        frames = 0
                        setzero = True
                    if setzero:
                        bullet2_image = tiles['Explosion']
                        """
                        if frames > 0 and frames < FPS * 0.5 * dT:
                            bullet2_image = tiles['Explosion']
                        elif frames > FPS * 0.5 * dT and frames < FPS * 0.525 * dT:
                            bullet2_image = tiles['ExplosionLarge']
                        else:
                            bullet2_image = tiles['0010B']"""


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            pygame.display.update()
            clock.tick(FPS)
            frames += 1
        preframes += 1



