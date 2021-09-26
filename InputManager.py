import pygame


def getdirec():
    keys = [False, False, False, False]
    if pygame.key.get_pressed()[pygame.K_d]:
        keys[0] = True
    elif pygame.key.get_pressed()[pygame.K_s]:
        keys[1] = True
    elif pygame.key.get_pressed()[pygame.K_a]:
        keys[2] = True
    elif pygame.key.get_pressed()[pygame.K_w]:
        keys[3] = True
    if True not in keys:
        return 0
    elif keys.count(True) > 1:
        return 0
    else:
        return keys.index(True) + 1
