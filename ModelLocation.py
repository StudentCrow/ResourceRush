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
    def __init__(self, name, x, y, functional = False, power = 0.0, temperature = 0.0):
        # self.image = pygame.image.load(img_path)    #Load sprite

        self.name = name
        self.functional = functional
        self.power = power
        self.temperature = temperature
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
            self.AlertCounter = {'TOO MUCH GRAPHICS': 0, 'LOW POWER': 0, 'HIGH TEMPERATURE': 0, 'GRAPHICS NOT WORKING': 0}
            self.graphics = 0.0
            self.consumption = 170.0
        elif self.name == 'VENT':
            pass

    def ManageAlerts(self):    #Method that generates alerts when the conditions are met
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
            ###
            #Random increase of graphics usage between 0% and 10%
            if self.AlertCounter['GRAPHICS NOT WORKING'] == 0: #Graphics only increase if working
                if self.graphics < 1:
                    self.graphics += round(uniform(0.0, 0.1),2)
                    if self.graphics > 1:
                        self.graphics += round(uniform(0.0, 0.01),2)    #Graphic usage rises slower because it will generate too much heat, aka, temperature error
            ###
            #Graphics errors
            if self.graphics >= 0.8 and self.AlertCounter['TOO MUCH GRAPHICS'] == 0:    #Activates the too much graphic usage alert
                self.AlertCounter['TOO MUCH GRAPHICS'] += 1
            elif self.graphics < 0.8 and self.AlertCounter['TOO MUCH GRAPHICS'] == 1:   #Deactivates the too much graphic usage alert
                self.AlertCounter['TOO MUCH GRAPHICS'] -= 1

            if self.graphics > 0.65 and self.AlertCounter['GRAPHICS NOT WORKING'] == 0: #Activates with a 15% chance the graphics not working error if graphic usage abive 65%
                error = random()
                if error > 0.85:
                    self.AlertCounter['GRAPHICS NOT WORKING'] += 1
                    self.graphics = 0
            ###
            #Temperature error
            if self.temperature >= 93.0 and self.AlertCounter['HIGH TEMPERATURE'] == 0:
                self.AlertCounter['HIGH TEMPERATURE'] += 1
            elif self.temperature < 93.0 and self.AlertCounter['HIGH TEMPERATURE'] == 1:
                self.AlertCounter['HIGH TEMPERATURE'] -= 1
            ###
            #Power error
            if self.power <= 425.0 and self.AlertCounter['LOW POWER'] == 0:
                self.AlertCounter['LOW POWER'] += 1
            elif self.power > 425.0 and self.AlertCounter['LOW POWER'] == 1:
                self.AlertCounter['LOW POWER'] -= 1
        elif self.name == 'VENT':
            pass

    def TempIncrease(self): #Method to calculate how much temperature does the location have
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
            if self.graphics <= 0.89:
                if self.temperature < 75:
                    self.temperature += 1
            else:
                self.temperature = self.consumption*(self.graphics - 0.89) + 75
        elif self.name == 'VENT':
            pass