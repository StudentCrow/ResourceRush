from random import *
from ModelBit import ModelBit
class ModelVRM:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.functional = False
        self.raw_power = 0.0
        self.temperature = 0.0
        self.power = 0.0
        self.alert_percentage = 0
        self.alert_counter = {'TEMPERATURE': 0, 'POWER': 0, 'VRM NW': 0}
        
    def resetLocation(self):
        self.functional = False; self.power = 0.0; self.temperature = 0.0
        for name in self.alert_counter:
            if name == 'VRM NW':
                self.alert_counter[name] = 0
                for i in ModelBit.instances:
                    if i.loc == self.name and i.subsystem:
                        i.subsystem = False
                        i.FixCheck = False
            else: self.alert_counter[name] = 0

    def manageAlerts(self):
        if self.functional:
            ###
            # Random VRM error
            if self.power > 500.0 and self.alert_counter['VRM NW'] == 0:
                error = round(random(), 2)
                if error > 0.95:  # 5% chance for the error to trigger
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

    def customAlert(self, bit):
        if self.functional:
            pass
        else:
            bit.subsystem = False
            bit.FixCheck = False