import pygame
import sys
import os
from Viewer_Menu import *
from Resources import *

pygame.init()

window = pygame.display.set_mode(WINDOW_DIM)
pygame.display.set_caption("Resource Rush")

pygame.draw.rect(window, WHITE, (0.5 * WIDTH, 0.5 * WIDTH, 5, 5), 5)




pygame.display.flip()
# bucle prueba
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()