import pygame
import time
from pygame.locals import *

class ViewOrder:
    def __init__(self, screen_res):
        self.font = pygame.font.SysFont('arial.ttf', 35)
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

    def drawOrderText(self, text, screen):
        text_image = self.font.render(text, True, (255, 255, 255))
        text_rect = text_image.get_rect(center=self.fill_rect.center)
        cursor = Rect(text_rect.topright, (3, text_rect.height))
        if time.time() % 1 > 0.5:
            pygame.draw.rect(screen, (255, 255, 255), cursor)
        screen.blit(text_image, text_rect)