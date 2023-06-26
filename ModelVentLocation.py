from random import *

class ModelVent:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.functional = False
        self.power = 0.0
        self.temperature = 0.0
        self.vent_num = 3.0
        self.rpm = 0.0  # Average rpm from 800 to 1000
        self.consumption = 3.0  # Consumption per vent
        self.alert_percentage = 0
        self.alert_counter = {'POWER': 0, 'TEMPERATURE': 0, 'VENT': 0}
        
    def resetLocation(self):
        self.functional = False; self.temperature = 0.0; self.rpm = 0.0
        for name in self.alert_counter:
            if name == 'TEMPERATURE': self.alert_counter[name] = 0
            
    def manageAlerts(self):
        if self.functional:
            ###
            # Decrease of rpm
            if self.rpm > 0:
                self.rpm -= 15.0 * self.vent_num
                if self.rpm < 0:
                    self.rpm = 0
            ###
            # Vent error
            if self.vent_num > 0:  # A vent error can happen only if there is at least 1 vent working
                error = round(random(), 2)
                if error > 0.95:  # 5% chance for the error to trigger
                    self.alert_counter['VENT'] += 1
                    self.vent_num -= 1.0
                    self.alert_percentage += 100
            ###
            # Temperature error
            if self.temperature >= -10.0 and self.alert_counter['TEMPERATURE'] == 0:
                self.alert_counter['TEMPERATURE'] += 1
            elif self.temperature < -10.0 and self.alert_counter['TEMPERATURE'] != 0:
                self.alert_counter['TEMPERATURE'] -= 1
            ###
            # Power error
            if self.power <= 22.5 and self.alert_counter['POWER'] == 0:
                self.alert_counter['POWER'] += 1
            elif self.power > 22.5 and self.alert_counter['POWER'] != 0:
                self.alert_counter['POWER'] -= 1
            ###
            
    def customAlert(self, bit):
        if self.functional:
            if self.alert_counter['VENT'] > 0 and bit.subsystem:
                self.alert_percentage -= randrange(0, 4)
                if self.alert_percentage <= 200 and self.alert_counter['VENT'] == 3:
                    self.alert_counter['VENT'] -= 1
                    self.vent_num += 1.0
                elif self.alert_percentage <= 100 and self.alert_counter['VENT'] == 2:
                    self.alert_counter['VENT'] -= 1
                    self.vent_num += 1.0
                elif self.alert_percentage <= 0 and self.alert_counter['VENT'] == 1:
                    if self.alert_percentage < 0: self.alert_percentage = 0
                    self.alert_counter['VENT'] -= 1
                    self.vent_num += 1.0
                    bit.subsystem = False
                    bit.FixCheck = False
            elif self.alert_counter['VENT'] == 0 and bit.subsystem:
                bit.subsystem = False
                bit.FixCheck = False
        else:
            bit.subsystem = False
            bit.FixCheck = False

    def tempIncrease(self):
        if self.functional:
            if self.rpm <= 2400.0:
                if self.temperature > -30.0: self.temperature -= 1.0
            else: self.temperature = -(self.consumption * (3.6 + self.rpm) + 30.0)
            
    def powerManagement(self):
        if self.power >= self.consumption * self.vent_num:
            if not self.functional: self.functional = True
            variable_consumption = (self.rpm / 1000) - 2.4
            if variable_consumption < 0: variable_consumption = 0
            self.power -= self.consumption * variable_consumption + self.consumption * self.vent_num
            if self.power < 0: self.power = 0
        else:
            self.resetLocation()
            
    def generateResource(self):
        if self.rpm < 2400.0:
            self.rpm += 50 * self.vent_num
        else:
            self.rpm += 10 * self.vent_num
        if self.rpm > 3000.0:
            self.rpm = 3000.0
            
    def getMined(self):
        if self.functional:
            if self.vent_num != 0: self.generateResource()

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