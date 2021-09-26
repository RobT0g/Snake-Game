import pygame
import PositionManager
import InputManager

pygame.init()
pygame.font.init()

# Images
board = pygame.image.load('Images/Frame.png')
snkh1 = pygame.image.load('Images/SnakeHead1.png')
snkh2 = pygame.image.load('Images/SnakeHead2.png')
snkh3 = pygame.image.load('Images/SnakeHead3.png')
snkh4 = pygame.image.load('Images/SnakeHead4.png')
snkb1 = pygame.image.load('Images/SnakeBody1.png')
snkb2 = pygame.image.load('Images/SnakeBody2.png')
snkt1 = pygame.image.load('Images/SnakeTail1.png')
snkt2 = pygame.image.load('Images/SnakeTail2.png')
snkbc = pygame.image.load('Images/CurveBody.png')
apple = pygame.image.load('Images/Apple.png')

# Auxiliares
pos = []
dtr = []
app = []
dead = False
times = 0
score = 0

# Texto
font1 = pygame.font.SysFont('Courier New', 32)
deathbox = pygame.Rect(80, 112, 16*32, 9*32)
deadtxt1 = font1.render(f'{"Game end!":^27}', False, (0, 0, 0))
deadtxt2 = font1.render(f'{"Press Space to restart":^27}', False, (0, 0, 0))
txt = f'Score: {score}'
deadtxt3 = font1.render(f'{txt:^27}', False, (0, 0, 0))


def initialize(screen):
    global pos, dtr, app, dead
    PositionManager.initialize()
    pos = actualpos(PositionManager.getpos())
    dtr = PositionManager.getdirtrain()
    app = actualpos(PositionManager.getapppos())
    dead = False
    PositionManager.resetdead()
    setonscreen(screen)


def update(ori):
    global times, pos, dtr, app, score
    PositionManager.update(ori)
    pos = actualpos(PositionManager.getpos())
    dtr = PositionManager.getdirtrain()
    app = actualpos(PositionManager.getapppos())
    score = PositionManager.getscore()
    times += 1
    if times == 4:
        times = 0


def setonscreen(screen):
    global pos, dtr, times, app, txt, deadtxt3
    screen.blit(board, (0, 0))
    screen.blit(apple, (app[0], app[1]))
    if not dead:
        for k, v in enumerate(dtr):
            imgs = []
            if k in (0, len(dtr)-1):
                if k == 0:
                    imgs = [snkh1, snkh2, snkh3, snkh4]
                elif k == len(dtr)-1:
                    imgs = [snkt1, snkt2, snkt1, snkt2]
                ang = -90 * (v - 1)
                blitrotim(imgs, ang, pos[k][0], pos[k][1], screen)
            else:
                if v in (1, 2):
                    imgs = [snkb1, snkb2, snkb1, snkb2]
                    ang = -90 * (v-1)
                else:
                    imgs = [snkbc, snkbc, snkbc, snkbc]
                    angs = [-90, 0, -180, -270]
                    ang = angs[v-3]
                blitrotim(imgs, ang, pos[k][0], pos[k][1], screen)
    else:
        pygame.draw.rect(screen, (19, 196, 181), deathbox)
        screen.blit(deadtxt1, (80, (5*32)+16))
        screen.blit(deadtxt2, (80, (8*32)+16))
        txt = f'Score: {score}'
        deadtxt3 = font1.render(f'{txt:^27}', False, (0, 0, 0))
        screen.blit(deadtxt3, (80, (7*32)+16))


def blitrotim(img, a, x, y, screen):
    global times
    if img:
        aux = pygame.transform.rotate(img[times-1], a)
    screen.blit(aux, (x, y))


def actualpos(posx):
    instpos = []
    if type(posx[0]) == int:
        instpos.append((posx[0] * 32) + 16)
        instpos.append((posx[1] * 32) + 16)
    else:
        for v in posx:
            instpos.append([(v[0]*32)+16, (v[1]*32)+16])
    return instpos


def getdead():
    global dead
    dead = PositionManager.getdead()
    return dead
