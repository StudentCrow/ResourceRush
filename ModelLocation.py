import pygame
from random import *

class ModelLocation:
    """
    Class for the model part of the interactive locations of the game
    """
    def __init__(self, name, x, y, functional = True, AlertNum = 0):
        # self.image = pygame.image.load(img_path)    #Load sprite

        self.name = name
        self.functional = functional
        self.AlertNum = AlertNum
        self.x = x
        self.y = y
        self.AlertNames = ['Alert1', 'Alert2', 'Alert3']
        self.AlertList = []

    def GenerateAlert(self):
        alert = choice(['Alert', 'NoAlert'])
        if alert == 'Alert':
            pass #Generate alert
        elif alert == 'NoAlert':
            pass #Does not generate alert