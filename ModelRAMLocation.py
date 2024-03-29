from random import *

class ModelRAM:
    def __init__(self, name, x, y):
        self.bit_list = []
        self.name = name
        self.x = x
        self.y = y
        self.functional = False
        self.power = 0.0
        self.temperature = 0.0
        self.available_ram = 16.0
        self.ram_in_use = 0.0
        self.consumption = 5.0
        self.alert = False
        self.alert_counter = {'POWER': 0, 'TEMPERATURE': 0, 'RAM': 0}
        
    def resetLocation(self):
        self.functional = False; self.temperature = 0.0; self.available_ram = 16.0; self.ram_in_use = 0.0
        for name in self.alert_counter:
            if name != 'POWER': self.alert_counter[name] = 0
    
    def manageAlerts(self):
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

    def customAlert(self, model_bit):
        for bit in self.bit_list:
            if bit.name == model_bit:
                bit.FixCheck = False

    def tempIncrease(self):
        if self.ram_in_use <= 2.0 and self.temperature < 40.0: self.temperature += 1.0
        elif self.ram_in_use > 2.0: self.temperature = self.consumption * (5.125 * (self.ram_in_use / 10)) + 40

    def powerManagement(self):
        self.power -= self.consumption
        if self.power < 0: self.power = 0

    def generateResource(self):
        ram_change = round(uniform(0.0, 0.5), 3)
        self.ram_in_use += ram_change; self.available_ram -= ram_change

    def getMined(self):
        if self.functional:
            ram_change = round(uniform(0.0, 0.1), 3)
            self.ram_in_use -= ram_change; self.available_ram += ram_change

    def getPower(self, name):  # Method for when a bit gives power to a location
        for bit in self.bit_list:
            if bit.name == name:
                charge = bit.load
                self.power += charge
                bit.load = 0

    def givePower(self, name):  # Method for when a bit gets power from a location
        for bit in self.bit_list:
            if bit.name == name:
                charge = bit.limit - bit.load
                self.power -= charge
                bit.load += charge

    def updateLocInfo(self):
        alerts = 0
        for a in self.alert_counter:
            alerts += self.alert_counter[a]
        info = {'P':self.power, 'T':self.temperature, 'R':self.available_ram, 'A':alerts}
        return info

    def work(self, loc_event):
        if self.functional:
            self.manageAlerts()
            self.tempIncrease()
        if self.power >= self.consumption and self.temperature < 81.0 and self.available_ram > 0.0:
            if not self.functional: self.functional = True
            if loc_event == 10: self.powerManagement()
        else:
            if self.functional: self.resetLocation()