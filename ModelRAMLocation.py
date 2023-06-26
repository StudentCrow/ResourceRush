from random import *

class ModelRAM:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.functional = False
        self.power = 0.0
        self.temperature = 0.0
        self.available_ram = 16.0
        self.ram_in_use = 0.0
        self.consumption = 5.0
        self.alert_counter = {'POWER': 0, 'TEMPERATURE': 0, 'RAM': 0}
        
    def resetLocation(self):
        self.functional = False; self.temperature = 0.0; self.available_ram = 16.0; self.ram_in_use = 0.0
        for name in self.alert_counter:
            if name != 'POWER': self.alert_counter[name] = 0
    
    def manageAlerts(self):
        if self.functional:
            ###
            # Random use of ram
            self.generateResource()
            ###
            # Ram error
            if self.available_ram <= 2.0 and self.alert_counter['RAM'] == 0:
                self.alert_counter['RAM'] += 1
            elif self.available_ram > 2.0 and self.alert_counter['RAM'] != 0:
                self.alert_counter['RAM'] -= 1
            ###
            # Temperature error
            if self.temperature >= 70.0 and self.alert_counter['TEMPERATURE'] == 0:
                self.alert_counter['TEMPERATURE'] += 1
            elif self.temperature < 70.0 and self.alert_counter['TEMPERATURE'] != 0:
                self.alert_counter['TEMPERATURE'] -= 1
            ###
            # Power error
            if self.power <= 12.5 and self.alert_counter['POWER'] == 0:
                self.alert_counter['POWER'] += 1
            elif self.power > 12.5 and self.alert_counter['POWER'] != 0:
                self.alert_counter['POWER'] -= 1
            ###

    def customAlert(self, bit):
        bit.subsystem = False
        bit.FixCheck = False

    def tempIncrease(self):
        if self.functional:
            if self.ram_in_use <= 2.0 and self.temperature < 40.0: self.temperature += 1.0
            elif self.ram_in_use > 2.0: self.temperature = self.consumption * (5.125 * (self.ram_in_use / 10)) + 40

    def powerManagement(self):
        if self.power >= self.consumption and self.temperature < 81.0:
            if not self.functional: self.functional = True
            self.power -= self.consumption
            if self.power < 0: self.power = 0
        else:
            self.resetLocation()

    def generateResource(self):
        ram_change = round(uniform(0.0, 0.5), 3)
        self.ram_in_use += ram_change; self.available_ram -= ram_change

    def getMined(self):
        if self.functional:
            ram_change = round(uniform(0.0, 0.1), 3)
            self.ram_in_use -= ram_change; self.available_ram += ram_change

    def get_power(self, bit):    #Method for when a bit gives power to a location
        charge = bit.load
        self.power += charge
        bit.load = 0

    def give_power(self, bit):  #Method for when a bit gets power from a location
        charge = bit.limit - bit.load
        self.power -= charge
        bit.load += charge

    def work(self):
        return ''