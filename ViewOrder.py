import pygame.draw
from pygame.locals import *

class ViewOrder:
    def __init__(self, screen_res):
        self.fill_color = (0, 0, 0)
        self.border_color = (255, 0, 0)
        self.collided_color = (0, 255, 0)
        self.fill_rect = Rect(screen_res.current_w-450, screen_res.current_h-100, 450, 100)
        self.border_rect = Rect(screen_res.current_w-450, screen_res.current_h-100, 450, 100)
        self.collided_rect = Rect(screen_res.current_w-450, screen_res.current_h-100, 450, 100)
        self.collided_check = False

    def drawOrder(self, screen):
        pygame.draw.rect(screen, self.fill_color, self.fill_rect)
        if not self.collided_check:
            pygame.draw.rect(screen, self.border_color, self.border_rect, 3)
        else:
            pygame.draw.rect(screen, self.collided_color, self.collided_rect, 3)

    def checkOrderCollision(self, mouse_pos):
        self.collided_check = pygame.Rect.collidepoint(self.fill_rect, mouse_pos)
        return self.collided_check