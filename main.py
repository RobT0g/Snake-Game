import pygame
from pygame.locals import *
import ScreenManager
import InputManager

pygame.init()

screen_width = 21*32                                                    # Screen width
screen_height = 16*32                                                   # Screen Height

screen = pygame.display.set_mode((screen_width, screen_height))         # Screen defined
pygame.display.set_caption('Pile')                                      # Screen name

walktime = 300                                                          # 250ms for each half tile walked
clock = pygame.time.Clock()                                             # Internal timer
move_event = pygame.USEREVENT + 1                                       # Move event defined
pygame.time.set_timer(move_event, walktime)                             # New event called each 250ms

ScreenManager.initialize(screen)                                        # Initial screen
pygame.display.flip()
orient = 0                                                              # Movement orientation aux
ori = 0                                                                 # Orientation aux
restart = False

running = True                                                          # Flux variable
while running:
    if (x := InputManager.getdirec()) != 0:
        if ((orient == 0) and (x in (1, 2, 4))) or ((orient != 0) and ((x % 2) != (orient % 2))):
            ori = x
    clock.tick(40)
    for event in pygame.event.get():
        if event.type == move_event:
            if not ScreenManager.getdead():
                orient = ori
                ScreenManager.update(orient)
                ScreenManager.setonscreen(screen)
                restart = False
            else:
                ScreenManager.setonscreen(screen)
                if restart:
                    ori = orient = 0
                    ScreenManager.initialize(screen)  # Initial screen
                    pygame.display.flip()
                    restart = False
            pygame.display.flip()
    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
        running = False
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        restart = True
