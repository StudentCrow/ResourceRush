import pygame
from pygame.locals import *

class ViewLocation:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.loc_rect = Rect(x-100, y-100, 200, 200)

    def drawLocation(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), self.loc_rect)