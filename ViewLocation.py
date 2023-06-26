import pygame
from pygame.locals import *

class ViewLocation:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.loc_rect = Rect(x-50, y-50, 100, 100)

    def drawLocation(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), self.loc_rect)