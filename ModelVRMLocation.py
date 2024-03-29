from random import *

class ModelVRM:
    def __init__(self, name, x, y):
        self.bit_list = []
        self.name = name
        self.x = x
        self.y = y
        self.functional = False
        self.raw_power = 0.0
        self.temperature = 0.0
        self.power = 0.0
        self.consumption = 5.0
        self.alert_percentage = 0
        self.alert = False
        self.alert_counter = {'TEMPERATURE': 0, 'POWER': 0, 'VRM NW': 0}
        
    def resetLocation(self):
        self.functional = False; self.power = 0.0; self.temperature = 0.0; self.alert_percentage = 0
        for name in self.alert_counter: self.alert_counter[name] = 0

    def manageAlerts(self):
        ###
        # Random VRM error
        if self.power > 500.0 and self.alert_counter['VRM NW'] == 0:
            error = random()
            if error > 0.95:  # 5% chance for the error to trigger
                self.alert = True
                self.alert_counter['VRM NW'] += 1
                self.power = 0.0
                self.alert_percentage = 100
        ###
        # Temperature error, at 120ºC it resets
        if self.temperature >= 90.0 and self.alert_counter['TEMPERATURE'] == 0:
            self.alert_counter['TEMPERATURE'] += 1
        elif self.temperature < 90.0 and self.alert_counter['TEMPERATURE'] != 0:
            self.alert_counter['TEMPERATURE'] -= 1
        ###
        # Refined power error
        if self.power >= 800.0 and self.alert_counter['POWER'] == 0:
            self.alert_counter['POWER'] += 1
        elif self.power < 800.0 and self.alert_counter['POWER'] != 0:
            self.alert_counter['POWER'] -= 1
        ###

    def customAlert(self, model_bit):
        for bit in self.bit_list:
            if bit.name == model_bit:
                if self.functional:
                    if self.alert_counter['VRM NW'] != 0 and bit.FixCheck:
                        self.alert_percentage -= randrange(0, 4)
                        if self.alert_percentage <= 0:  # If there is no more error to be fixed, it gets deleted and the bit exits the subsystem
                            if self.alert_percentage < 0: self.alert_percentage = 0
                            self.alert_counter['VRM NW'] -= 1
                            self.alert = False
                            bit.FixCheck = False
                    elif self.alert_counter['VRM NW'] == 0 and bit.FixCheck:  # In case there were more than one bit working to fix the error and it is already fixed, they get dismissed from the task
                        bit.FixCheck = False
                else:
                    bit.FixCheck = False
            
    def tempIncrease(self):
        if self.power <= 100.0 and self.temperature < 60.0: self.temperature += 1.0
        elif self.power > 100.0: self.temperature = 10.0 * (6.0 * (self.power / 1000.0)) + 60.0

    def powerManagement(self):
        self.power -= self.consumption

    def generateResource(self):
        if self.raw_power >= 100.0:
            self.raw_power -= 100; self.power += 10

    def getMined(self):
        self.generateResource()

    def getPower(self, name):  # Method for when a bit gives power to a location
        for bit in self.bit_list:
            if bit.name == name:
                charge = bit.load
                self.raw_power += charge
                bit.load = 0

    def givePower(self, name):  # Method for when a bit gets power from a location
        for bit in self.bit_list:
            if bit.name == name:
                charge = bit.limit - bit.load
                self.raw_power -= charge

    def updateLocInfo(self):
        alerts = 0
        for a in self.alert_counter:
            alerts += self.alert_counter[a]
        info = {'P':self.power, 'T':self.temperature, 'RP':self.raw_power, 'A':alerts, 'AP':self.alert_percentage}
        return info

    def work(self, loc_event):
        if self.functional:
            self.manageAlerts()
            self.tempIncrease()
        if self.temperature < 120.0 and self.power >= self.consumption:
            if not self.functional: self.functional = True
            if loc_event == 10: self.powerManagement()
        else:
            if self.functional: self.resetLocation()