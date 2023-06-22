from Imports import *

class ViewerBit:
    def __init__(self, display, x = 0, y = 0, mult = 0, fill_color = (255, 255, 255)):
        self.display = display
        self.x = x
        self.y = y
        self.mult = mult
        self.fill_color = fill_color
        self.border_color = (0, 0, 0)

    #Function to draw the full bit
    def draw_bit(self):
        bit_fill = pygame.draw.rect(self.display, self.fill_color, (self.x, self.y, 50, 50), 0)
        bit_border = pygame.draw.rect(self.display, self.border_color, (self.x, self.y, 50, 50), 2)