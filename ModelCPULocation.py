from random import *

class ModelCPU:
    def __init__(self, name, x, y):
        self.bit_list = []
        self.name = name
        self.x = x
        self.y = y
        self.functional = False
        self.temperature = 0.0
        self.power = 0.0
        self.processes = 0.0
        self.consumption = 20.0
        self.alert = False
        self.alert_counter = {'power raw_power': 0, 'TEMPERATURE': 0, 'PROCESSES': 0}

    def resetLocation(self):
        self.functional = False; self.temperature = 0.0
        for name in self.alert_counter:
            if name == 'TEMPERATURE': self.alert_counter[name] = 0

    def manageAlerts(self):
        ###
        # Random processes increase
        self.generateResource()
        ###
        # Processes error
        if self.processes >= 90.0 and self.alert_counter['PROCESSES'] == 0:
            self.alert_counter['PROCESSES'] += 1
        elif self.processes < 90.0 and self.alert_counter['PROCESSES'] != 0:
            self.alert_counter['PROCESSES'] -= 1
        ###
        # Temperature error
        if self.temperature >= 45.0 and self.alert_counter['TEMPERATURE'] == 0:
            self.alert_counter['TEMPERATURE'] += 1
        elif self.temperature < 45.0 and self.alert_counter['TEMPERATURE'] != 0:
            self.alert_counter['TEMPERATURE'] -= 1
        ###
        # raw_power error
        if self.power <= 50 and self.alert_counter['power raw_power'] == 0:
            self.alert_counter['power raw_power'] += 1
        elif self.power > 50 and self.alert_counter['power raw_power'] != 0:
            self.alert_counter['power raw_power'] -= 1

    def customAlert(self, model_bit):
        for bit in self.bit_list:
            if bit.name == model_bit:
                if bit.FixCheck: bit.FixCheck = False

    def tempIncrease(self):
        if self.processes <= 20.0 and self.temperature < 30.0: self.temperature += 1.0
        elif self.processes > 20.0: self.temperature = self.consumption * (1 * (self.processes / 100)) + 30

    def powerManagement(self):
        self.power -= self.consumption
        if self.power < 0: self.power = 0

    def generateResource(self):
        self.processes += randrange(1, 6)

    def getMined(self):
        if self.functional and self.processes != 0:
            self.processes -= randrange(1, 3)
            if self.processes < 0: self.processes = 0.0

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
        info = {'P':self.power, 'T':self.temperature, 'Pr':self.processes, 'A':alerts}
        return info

    def work(self, loc_event):
        if self.functional:
            self.manageAlerts()
            self.tempIncrease()
        if self.power >= self.consumption and self.temperature < 50.0:
            if not self.functional: self.functional = True
            if loc_event == 10: self.powerManagement()
        else:
            if self.functional: self.resetLocation()