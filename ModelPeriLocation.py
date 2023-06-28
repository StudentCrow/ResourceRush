from random import *

class ModelPERI:
    def __init__(self, name, x, y):
        self.bit_list = []
        self.name = name
        self.x = x
        self.y = y
        self.functional = False
        self.power = 0.0
        self.temperature = 0.0
        self.peri_num = 4.0
        self.consumption = 10.0
        self.alert_percentage = 0
        self.alert = False
        self.alert_counter = {'POWER': 0, 'TEMPERATURE': 0, 'PERIPHERAL': 0}

    def resetLocation(self):
        self.functional = False; self.temperature = 0.0
        for name in self.alert_counter:
            if name == 'TEMPERATURE': self.alert_counter[name] = 0

    def manageAlerts(self):
        ###
        # Consume of chipset power
        self.generateResource()
        ###
        # Random peripheral error
        if self.peri_num > 0 and model_CHIPSET.chipset_power < 25.0:  # A peripheral error cna happen only if there is at least 1 peripheral working and there is low chipset power
            error = random()
            if error > 0.95:  # There's 5% chance of it triggering
                if not self.alert: self.alert = True
                self.alert_counter['PERIPHERAL'] += 1
                self.peri_num -= 1.0
                self.alert_percentage += 100
        ###
        # Temperature error
        if self.temperature >= 5.0 * self.peri_num and self.alert_counter['TEMPERATURE'] == 0:
            self.alert_counter['TEMPERATURE'] += 1
        elif self.temperature < 5.0 * self.peri_num and self.alert_counter['TEMPERATURE'] != 0:
            self.alert_counter['TEMPERATURE'] -= 1
        ###
        # Power error
        if self.power <= 100.0 and self.alert_counter['POWER'] == 0:
            self.alert_counter['POWER'] += 1
        elif self.power > 100.0 and self.alert_counter['POWER'] != 0:
            self.alert_counter['POWER'] -= 1
        ###
            
    def customAlert(self, model_bit):
        for bit in self.bit_list:
            if bit.name == model_bit:
                if self.functional:
                    if self.alert_counter['PERIPHERAL'] > 0 and bit.FixCheck:
                        self.alert_percentage -= randrange(0, 4)
                        if self.alert_percentage <= 300 and self.alert_counter['PERIPHERAL'] == 4:
                            self.alert_counter['PERIPHERAL'] -= 1
                            self.peri_num += 1.0
                        elif self.alert_percentage == 0 and self.alert_counter['VENT NOT WORKING'] == 3:
                            self.alert_counter['PERIPHERAL'] -= 1
                            self.peri_num += 1.0
                        elif self.alert_percentage <= 100 and self.alert_counter['VENT NOT WORKING'] == 2:
                            self.alert_counter['PERIPHERAL'] -= 1
                            self.peri_num += 1.0
                        elif self.alert_percentage <= 0 and self.alert_counter['VENT NOT WORKING'] == 1:
                            if self.alert_percentage < 0: self.alert_percentage = 0
                            self.alert_counter['PERIPHERAL'] -= 1
                            self.peri_num += 1.0
                            self.alert = False
                            bit.FixCheck = False
                else:
                    bit.FixCheck = False
            
    def tempIncrease(self):
        if model_CHIPSET.chipset_power > 0.0:
            if self.temperature < 5.0 * self.peri_num:
                self.temperature += 0.2
        else: self.temperature = 10.0 * self.peri_num
            
    def powerManagement(self):
        variable_consumption = (1.0 - (model_CHIPSET.chipset_power / 100))
        if variable_consumption < 0: variable_consumption = 0
        self.power -= (self.consumption * variable_consumption) * self.peri_num + self.consumption * self.peri_num
        if self.power < 0: self.power = 0
            
    def generateResource(self):
         if model_CHIPSET.chipset_power != 0:
            model_CHIPSET.chipset_power -= round(uniform(0.0, 2.0), 2)*self.peri_num
            if model_CHIPSET.chipset_power < 0: model_CHIPSET.chipset_power = 0.0

    def getMined(self):
        return ''

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
        info = {'P':self.power, 'T':self.temperature, 'PN':self.peri_num, 'A':alerts, 'AP':self.alert_percentage}
        return info

    def work(self, loc_event):
        if self.functional:
            self.manageAlerts()
            self.tempIncrease()
        if self.power >= self.consumption * self.peri_num:
            if not self.functional: self.functional = True
            if loc_event == 10: self.powerManagement()
        else:
            if self.functional: self.resetLocation()