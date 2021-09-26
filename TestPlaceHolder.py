import pygame

screen = pygame.display.set_mode((400, 400))         # Screen defined
img = pygame.image.load('Images/SnakeHead1.png')
screen.blit(img, (0, 0))
ang = 0
pos = 32
for v in range(3):
    ang -= 90
    aux = pygame.transform.rotate(img, ang)
    aux = pygame.transform.flip(aux, False, True)
    screen.blit(aux, (pos, pos))
    pos += 32
pygame.display.flip()
while not pygame.key.get_pressed()[pygame.K_ESCAPE]:
    pygame.event.wait()
