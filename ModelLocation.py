import pygame
from random import *
from ModelAlert import *

class ModelLocation:
    """
    Class for the model part of the interactive locations of the game
    """
    # Condicional para comprobar que localicación es y por lo tanto cambiar su comportamiento
    # if self.name == 'PERI':
    #     pass
    # elif self.name == 'VRM':
    #     pass
    # elif self.name == 'RAM':
    #     pass
    # elif self.name == 'ATX':
    #     pass
    # elif self.name == 'CPU':
    #     pass
    # elif self.name == 'DISK':
    #     pass
    # elif self.name == 'CLK':
    #     pass
    # elif self.name == 'BIOS':
    #     pass
    # elif self.name == 'CHIPSET':
    #     pass
    # elif self.name == 'GPU':
    #     pass
    # elif self.name == 'VENT':
    #     pass
    def __init__(self, name, x, y, functional = True, AlertNum = 0):
        # self.image = pygame.image.load(img_path)    #Load sprite

        self.name = name
        self.functional = functional
        self.AlertNum = AlertNum
        self.x = x
        self.y = y

        #Different alerts depending on the location:
        if self.name == 'PERI':
            pass
        elif self.name == 'VRM':
            pass
        elif self.name == 'RAM':
            pass
        elif self.name == 'ATX':
            pass
        elif self.name == 'CPU':
            pass
        elif self.name == 'DISK':
            pass
        elif self.name == 'CLK':
            pass
        elif self.name == 'BIOS':
            pass
        elif self.name == 'CHIPSET':
            pass
        elif self.name == 'GPU':
            self.AlertNames = ['TOO MUCH GRAPHICS', 'LOW VOLTAGE', 'HIGH TEMPERATURE', 'GRAPHICS NOT WORKING']
        elif self.name == 'VENT':
            pass

    def GenerateAlert(self):    #Method that generates alerts when the conditions are met
        if self.name == 'PERI':
            pass
        elif self.name == 'VRM':
            pass
        elif self.name == 'RAM':
            pass
        elif self.name == 'ATX':
            pass
        elif self.name == 'CPU':
            pass
        elif self.name == 'DISK':
            pass
        elif self.name == 'CLK':
            pass
        elif self.name == 'BIOS':
            pass
        elif self.name == 'CHIPSET':
            pass
        elif self.name == 'GPU':
            pass
        elif self.name == 'VENT':
            pass