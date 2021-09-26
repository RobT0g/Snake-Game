import InputManager
from random import shuffle


pos = [[10, 10], [9, 10]]                           # Position on-grid
dirtrain = []                                       # Orientation for set on screen
grid = []                                           # Grid state
applepos = []                                       # Apple position
dead = False
orient = 0      # Orientation. 1: Right; 2: Down; 3: Left; 4: Up.
strtmove = False


def initialize():
    global pos, orient
    pos = [[9, 10], [8, 10], [7, 10], [6, 10]]  # Position ongrid
    orient = 0
    getdirtrain()
    gridstate()
    setapplepos()


def update(ori):
    global strtmove, orient
    orient = ori
    if orient != 0:
        nexttile()
        gridstate()
        dectgrow()


def getscore():
    global pos
    return (len(pos)-4)*100


def nexttile():
    global orient, pos
    if orient == 1:
        pos.insert(0, [pos[0][0] + 1, pos[0][1]])
    elif orient == 2:
        pos.insert(0, [pos[0][0], pos[0][1] + 1])
    elif orient == 3:
        pos.insert(0, [pos[0][0] - 1, pos[0][1]])
    elif orient == 4:
        pos.insert(0, [pos[0][0], pos[0][1] - 1])
    # print(pos)
    pos.pop()
    posfilter()


def posfilter():
    global pos, dead
    for k, v in enumerate(pos):
        if k != 0 and pos[0] == v:
            dead = True
        if (y := v[1]) not in range(0, 15):
            if y <= -1:
                v[1] = 15+y
            elif y >= 15:
                v[1] = -15+y
        elif (x := v[0]) not in range(0, 20):
            if x <= -1:
                v[0] = 20+x
            elif x >= 20:
                v[0] = -20+x


def getdirtrain():
    # This defines how to set the snake pieces on the screen
    global dirtrain, pos
    dirtrain = []
    for k, v in enumerate(pos):
        if k == 0:
            if orient != 0:
                dirtrain.append(orient)
            else:
                dirtrain.append(1)
        elif k == len(pos)-1:
            dirtrain.append(directaux(v, pos[k-1]))
        else:
            dirtrain.append(directaux(v, pos[k-1], pos[k+1]))
    return dirtrain


def getdead():
    global dead
    return dead


def resetdead():
    global dead
    dead = False


def directaux(p, p0, p1=()):
    if not p1:              # If this parameter does not enter here, it means we are checking for the tail
        # This returns from 1 to 4 based on the tail orientation. 1 means right, and clockwise for the rest
        if p0[0] - p[0] != 0:
            return 2 - (p0[0] - p[0])
        elif p0[1] - p[1] != 0:
            return 3 - (p0[1] - p[1])
    else:                   # If the parameter did enter, it means we are checking for a body part
        x1 = mod(p0[0] - p[0])
        x2 = mod(p1[0] - p[0])
        y1 = mod(p0[1] - p[1])
        y2 = mod(p1[1] - p[1])
        if (x1 != 0) and (x2 != 0):         # If both the previous and next pieces are located on the x diff
            return 1
        elif (y1 != 0) and (y2 != 0):       # If both the previous and next pieces are located on the y diff
            return 2
        elif (y1 == -1) or (y2 == -1):      # If one of the neighbour piece is up
            if (x1 == 1) or (x2 == 1):          # If the other one is to the right
                return 3                            # Connection Up to Right
            elif (x1 == -1) or (x2 == -1):        # If the other one is to the left
                return 4                            # Connection Up to left
        elif (y1 == 1) or (y2 == 1):        # If one of the neighbour piece is down
            if (x1 == 1) or (x2 == 1):          # If the other piece is to the right
                return 5                            # Connection Down to Right
            elif (x1 == -1) or (x2 == -1):      # If the other piece is to the left
                return 6                            # Connection Down to Left


def mod(x):
    # This allows the cases on whose the snake is divided to calculate the link angle
    if x in (-1, 0, 1):
        return x
    elif x < -1:
        return 1
    else:
        return -1


def gridstate():
    # This allows to quickly recognize a tile where there's a snake piece
    global grid, pos, applepos
    grid = []
    for v in range(20):
        grid.append([])
        for i in range(15):
            grid[v].append(0)
    for k, v in enumerate(pos):
        grid[v[0]][v[1]] = 1


def setapplepos():
    # This makes the apple appear in a random position inside the grid
    global applepos, grid
    instfs = []
    for x, v1 in enumerate(grid):
        for y, v2 in enumerate(v1):
            if v2 == 0:
                instfs.append([x, y])       # Register the free tiles
    shuffle(instfs)                         # Shuffle them
    applepos = instfs[0]                    # Get an item from it
    grid[applepos[0]][applepos[1]] = 2


def getapppos():
    global applepos
    return applepos


def dectgrow():
    global pos, applepos, dirtrain
    if pos[0] == applepos:
        if (ot := dirtrain[-1]) == 1:
            pos.append([pos[-1][0]-1, pos[-1][1]])
        elif ot == 2:
            pos.append([pos[-1][0], pos[-1][1]-1])
        elif ot == 3:
            pos.append([pos[-1][0]+1, pos[-1][1]])
        else:
            pos.append([pos[-1][0], pos[-1][1]+1])
        posfilter()
        gridstate()
        setapplepos()
        getdirtrain()


def getpos():
    global pos
    return pos
