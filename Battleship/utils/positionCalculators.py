import math

def calculateShipPositions(ships, cell_size, boardpos, turrentsize):
    ships_pos = []
    for ship in ships:
        pos = []
        #Posx = board_x+cell_x+(cell_size-turrentsize)/2
        """
        pos.append(boardpos[0]+(ship[0]*cell_size)+(cell_size*ship[3]*math.cos((math.pi/2)*ship[2])/2))
        pos.append(boardpos[1]+(ship[1]*cell_size)+(cell_size*ship[4]*math.cos((math.pi/2)*ship[2])/2))
        pos[0] -= turrentsize/2
        pos[1] -= turrentsize/2"""

        #Setting Grid Position
        pos.append(boardpos[0]+(ship[0]*cell_size))
        pos.append(boardpos[1]+(ship[1]*cell_size))

        #Setting up position within ship
        pos[0] += ((cell_size * ship[3]) - turrentsize) / 2
        pos[1] += ((cell_size * ship[4]) - turrentsize) / 2


        ships_pos.append(pos)

    return ships_pos