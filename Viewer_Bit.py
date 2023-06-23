import pygame.draw

from Imports import *

class ViewerBit:
    def __init__(self, display, x = 0, y = 0, mult = 0, fill_color = (255, 255, 255)):
        self.display = display
        self.x = x
        self.y = y
        self.chonky = 50
        self.mult = mult
        self.fill_color = fill_color
        self.border_color = (0, 0, 0)
        self.bit_selected = False

    #Function to draw the full bit
    def drawBit(self):
        bit_fill = pygame.draw.rect(self.display, self.fill_color, (self.x, self.y, self.chonky, self.chonky), 0)
        bit_border = pygame.draw.rect(self.display, self.border_color, (self.x, self.y, self.chonky, self.chonky), 5)
        if self.bit_selected:
            bit_selection = pygame.draw.rect(self.display, (255, 255, 0), (self.x, self.y, self.chonky, self.chonky), 2)

    #Function to check if a bit is being selected
    def checkBitSelection(self, first_pos, last_pos):
        x_list = [first_pos[0], last_pos[0]]
        x_list.sort()
        y_list = [first_pos[1], last_pos[1]]
        y_list.sort()
        if self.x <= x_list[1] and self.x >= x_list[0]:
            if self.y <= y_list[1] and self.y >= y_list[0]:
                self.bit_selected = True
            else:
                self.bit_selected = False
        else:
            self.bit_selected = False