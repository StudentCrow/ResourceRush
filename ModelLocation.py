import pygame

class ModelLocation:
    """
    Class for the model part of the interactive locations of the game
    """
    def __init__(self, name, x, y, functional = True, AlertNum = 0):
        self.name = name
        self.functional = functional
        self.AlertNum = AlertNum
        self.x = x
        self.y = y
        #self.AlertList = , still to determine the type of alerts a location can have