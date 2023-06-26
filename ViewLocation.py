import pygame
from pygame.locals import *

class ViewLocation:
    def __init__(self, name, x, y):
        self.font = pygame.font.SysFont('arial', 35)
        self.info_font = pygame.font.SysFont('arial', 25)
        self.name = name
        self.x = x
        self.y = y
        self.size = 100
        self.loc_rect = Rect(self.x - self.size, self.y - self.size, self.size*2, self.size*2)
        self.text_color = (255, 255, 255)
        self.info_color = (0, 0, 0)
        self.off_color = (255, 0, 0)
        self.on_color = (0, 255, 0)
        self.collided_check = False

    def drawLocation(self, screen, functional = bool):
        if not functional:
            pygame.draw.rect(screen, self.off_color, self.loc_rect)
        else:
            pygame.draw.rect(screen, self.on_color, self.loc_rect)
        text_image = self.font.render(self.name, True, self.text_color)
        text_rect = text_image.get_rect(center=self.loc_rect.center)
        screen.blit(text_image, text_rect)

    def showFont(self, screen, text):
        text_image = self.info_font.render(str(text), True, self.info_color)
        text_rect = text_image.get_rect(center=(self.x, self.y-self.size-15))
        screen.blit(text_image, text_rect)

    def checkLocationCollision(self, mouse_pos):
        self.collided_check = pygame.Rect.collidepoint(self.loc_rect, mouse_pos)

    def zoomLocation(self, direction):
        min_size = 50
        max_size = 250
        if direction == 1 and self.size < max_size:
            self.size += 10
        elif direction == -1 and self.size > min_size:
            self.size -= 10
        self.loc_rect = Rect(self.x - self.size, self.y - self.size, self.size * 2, self.size*2)