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
        pass