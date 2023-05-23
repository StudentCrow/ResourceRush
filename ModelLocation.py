import pygame
from random import *
from ModelAlert import *
from ModelBit import ModelBit

class InvalidFix(Exception):
    """
    Custom error for when a fix method is called but there is not an available error to be fixed
    """
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

class MiningError(Exception):
    """
    Custom error for when the mining method gets called but mining in the location is not possible at the moment
    """
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

class FunctionalityError(Exception):
    """
    Custom error for when the mining method gets called but mining in the location is not possible at the moment
    """
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

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
    def __init__(self, name, x, y, power=0.0, temperature=0.0, functional=False):
        # self.image = pygame.image.load(img_path)    #Load sprite

        self.name = name
        self.functional = functional
        self.power = power
        self.temperature = temperature
        self.x = x
        self.y = y

        #Different alerts and variables depending on the location:
        if self.name == 'PERI':
            self.AlertCounter = {'LOW POWER': 0, 'HIGH TEMPERATURE': 0, 'PERIPHERAL NOR WORKING': 0}
            self.CustomAlertPercentage = 0
            self.PeriNum = 4.0  #Each peripheral can only go up to 10ºC, 40ºC
            self.consumption = 10.0 #Consumption per peripheral
        elif self.name == 'VRM':
            self.AlertCounter = {'HIGH TEMPERATURE': 0, 'TOO MUCH REFINED POWER': 0, 'VRM NOT WORKING': 0}
            self.CustomAlertPercentage = 0
            self.refined_power = 0.0
        elif self.name == 'RAM':
            self.AlertCounter = {'LOW POWER': 0, 'HIGH TEMPERATURE': 0, 'LOW AVAILABLE RAM': 0}
            self.available_ram = 16.0
            self.ram_in_use = 0.0
            self.consumption = 5.0
        elif self.name == 'ATX':
            self.AlertCounter = {'TOO MUCH STORED POWER': 0}
            self.stored_power = 0.0
        elif self.name == 'CPU':
            self.AlertCounter = {'LOW REFINED POWER': 0, 'HIGH TEMPERATURE': 0, 'TOO MANY PROCESSES': 0}
            self.refined_power = 0.0
            self.processes = 0.0
            self.consumption = 20.0
        elif self.name == 'DISK':
            pass
        elif self.name == 'CLK':    #Let's you slow down time, let it for the last one as it will be linked with the control of time
            pass
        elif self.name == 'BIOS': #Bios should be always functional
            self.AlertCounter = {'BIOS NOT WORKING': 0}
            self.CustomAlertPercentage = 0
            self.BitBuilding = 0.0
        elif self.name == 'CHIPSET':
            self.AlertCounter = {'LOW CHIPSET OUTPUT': 0, 'LOW POWER': 0, 'HIGH TEMPERATURE': 0}
            self.chipset_power = 0.0
            self.consumption = 8.55
        elif self.name == 'GPU':
            self.AlertCounter = {'TOO MUCH GRAPHICS': 0, 'LOW POWER': 0, 'HIGH TEMPERATURE': 0, 'GRAPHICS NOT WORKING': 0}
            self.CustomAlertPercentage = 0
            self.graphics = 0.0
            self.consumption = 170.0
        elif self.name == 'VENT':
            self.AlertCounter = {'LOW POWER': 0, 'HIGH TEMPERATURE': 0, 'VENT NOT WORKING': 0}
            self.CustomAlertPercentage = 0
            self.VentNum = 3.0
            self.rpm = 0.0  # Average rpm from 800 to 1000
            self.consumption = 3.0  #Consumption per vent

    def reset_location(self):   #Method that resets everything for when it gets turned on or off
        if self.name == 'PERI':
            self.functional = False
            self.temperature = 0.0
            if self.AlertCounter['HIGH TEMPERATURE'] == 1:
                self.AlertCounter['HIGH TEMPERATURE'] -= 1
        elif self.name == 'VRM':
            self.functional = False
            self.refined_power = 0.0
            self.temperature = 0.0
            if self.AlertCounter['HIGH TEMPERATURE'] == 1:
                self.AlertCounter['HIGH TEMPERATURE'] -= 1
            if self.AlertCounter['TOO MUCH REFINED POWER'] == 1:
                self.AlertCounter['TOO MUCH REFINED POWER'] -= 1
            if self.AlertCounter['VRM NOT WORKING'] == 1:
                self.CustomAlertPercentage = 0
                self.AlertCounter['VRM NOT WORKING'] -= 1
                for i in ModelBit.instances:
                    if i.loc == self.name and i.subsystem:
                        i.subsystem = False
                        i.FixCheck = False
        elif self.name == 'RAM':
            self.functional = False
            self.temperature = 0.0
            self.available_ram = 16.0
            self.ram_in_use = 0.0
            self.manage_alerts()
        elif self.name == 'ATX':
            self.stored_power = 0.0
            if self.AlertCounter['TOO MUCH STORED POWER'] == 1:
                self.AlertCounter['TOO MUCH STORED POWER'] -= 1
        elif self.name == 'CPU':
            self.functional = False
            self.temperature = 0.0
            self.manage_alerts()
        elif self.name == 'DISK':
            pass
        elif self.name == 'CLK':
            pass
        elif self.name == 'BIOS':   #Is always functional
            pass
        elif self.name == 'CHIPSET':
            self.functional = False
            self.temperature = 0.0
            self.chipset_power = 0.0
            if self.AlertCounter['HIGH TEMPERATURE'] == 1:
                self.AlertCounter['HIGH TEMPERATURE'] -= 1
        elif self.name == 'GPU':
            self.functional = False
            self.temperature = 0.0
            self.graphics = 0.0
            if self.AlertCounter['HIGH TEMPERATURE'] == 1:
                self.AlertCounter['HIGH TEMPERATURE'] -= 1
            if self.AlertCounter['TOO MUCH GRAPHICS'] == 1:
                self.AlertCounter['TOO MUCH GRAPHICS'] -= 1
        elif self.name == 'VENT':
            self.functional= False
            self.temperature = 0.0
            self.rpm = 0.0

    def manage_alerts(self):    #Method that generates alerts when the conditions are met
        if self.functional:
            if self.name == 'PERI':
                ###
                #Consume of chipset power
                self.generate_resource()
                ###
                #Random peripheral error
                if self.PeriNum > 0 and CHIPSET.chipset_power < 25.0:    #A peripheral error cna happen only if there is at least 1 peripheral working and there is low chipset power
                    error = round(random(), 2)
                    if error > 0.95:    #There's 5% chance of it triggering
                        self.AlertCounter['PERIPHERAL NOT WORKING'] += 1
                        self.PeriNum -= 1.0
                        self.CustomAlertPercentage += 100
                ###
                #Temperature error
                if self.temperature >= 5.0*self.PeriNum and self.AlertCounter['HIGH TEMPERATURE'] == 0:
                    self.AlertCounter['HIGH TEMPERATURE'] += 1
                elif self.temperature < 5.0*self.PeriNum and self.AlertCounter['HIGH TEMPERATURE'] == 1:
                    self.AlertCounter['HIGH TEMPERATURE'] -= 1
                ###
                #Power error
                if self.power <= 100.0 and self.AlertCounter['LOW POWER'] == 0:
                    self.AlertCounter['LOW POWER'] += 1
                elif self.power > 100.0 and self.AlertCounter['LOW POWER'] == 1:
                    self.AlertCounter['LOW POWER'] -= 1
                ###
            elif self.name == 'VRM':
                ###
                #Random VRM error
                if self.refined_power > 500.0 and self.AlertCounter['VRM NOT WORKING'] == 0:
                    error = round(random(), 2)
                    if error > 0.95:    #5% chance for the error to trigger
                        self.AlertCounter['VRM NOT WORKING'] += 1
                        self.refined_power = 0.0
                        self.CustomAlertPercentage = 100
                ###
                #Temperature error, at 120ºC it resets
                if self.temperature >= 90.0*self.PeriNum and self.AlertCounter['HIGH TEMPERATURE'] == 0:
                    self.AlertCounter['HIGH TEMPERATURE'] += 1
                elif self.temperature < 90.0*self.PeriNum and self.AlertCounter['HIGH TEMPERATURE'] == 1:
                    self.AlertCounter['HIGH TEMPERATURE'] -= 1
                ###
                #Refined power error
                if self.refined_power >= 800.0 and self.AlertCounter['TOO MUCH REFINED POWER'] == 0:
                    self.AlertCounter['TOO MUCH REFINED POWER'] += 1
                elif self.refined_power < 800.0 and self.AlertCounter['TOO MUCH REFINED POWER'] == 1:
                    self.AlertCounter['TOO MUCH REFINED POWER'] -= 1
                ###
            elif self.name == 'RAM':
                ###
                #Random use of ram
                self.generate_resource()
                ###
                #Ram error
                if self.available_ram <= 2.0 and self.AlertCounter['LOW AVAILABLE RAM'] == 0:
                    self.AlertCounter['LOW AVAILABLE RAM'] += 1
                elif self.available_ram > 2.0 and self.AlertCounter['LOW AVAILABLE RAM'] == 1:
                    self.AlertCounter['LOW AVAILABLE RAM'] -= 1
                ###
                #Temperature error
                if self.temperature >= 70.0 and self.AlertCounter['HIGH TEMPERATURE'] == 0:
                    self.AlertCounter['HIGH TEMPERATURE'] += 1
                elif self.temperature < 70.0 and self.AlertCounter['HIGH TEMPERATURE'] == 1:
                    self.AlertCounter['HIGH TEMPERATURE'] -= 1
                ###
                #Power error
                if self.power <= 12.5 and self.AlertCounter['LOW POWER'] == 0:
                    self.AlertCounter['LOW POWER'] += 1
                elif self.power > 12.5 and self.AlertCounter['LOW POWER'] == 1:
                    self.AlertCounter['LOW POWER'] -= 1
                ###
            elif self.name == 'ATX':
                ###
                #Stored power error
                if self.stored_power >= 3500.0 and self.AlertCounter['TOO MUCH STORED POWER'] == 0:
                    self.AlertCounter['TOO MUCH STORED POWER'] += 1
                elif self.stored_power < 3500.0 and self.AlertCounter['TOO MUCH STORED POWER'] == 1:
                    self.AlertCounter['TOO MUCH STORED POWER'] -= 1
                ###
            elif self.name == 'CPU':
                ###
                #Random processes increase
                self.generate_resource()
                ###
                #Processes error
                if self.processes >= 90.0 and self.AlertCounter['TOO MANY PROCESSES'] == 0:
                    self.AlertCounter['TOO MANY PROCESSES'] += 1
                elif self.processes < 90.0 and self.AlertCounter['TOO MANY PROCESSES'] == 1:
                    self.AlertCounter['TOO MANY PROCESSES'] -= 1
                ###
                #Temperature error
                if self.temperature >= 45.0 and self.AlertCounter['HIGH TEMPERATURE'] == 0:
                    self.AlertCounter['HIGH TEMPERATURE'] += 1
                elif self.temperature < 45.0 and self.AlertCounter['HIGH TEMPERATURE'] == 1:
                    self.AlertCounter['HIGH TEMPERATURE'] -= 1
                ###
                #Power error
                if self.refined_power <= 50 and self.AlertCounter['LOW REFINED POWER'] == 0:
                    self.AlertCounter['LOW REFINED POWER'] += 1
                elif self.refined_power > 50 and self.AlertCounter['LOW REFINED POWER'] == 1:
                    self.AlertCounter['LOW REFINED POWER'] -= 1
            elif self.name == 'DISK':
                pass
            elif self.name == 'CLK':    #Pass por ahora
                pass
            elif self.name == 'BIOS':
                ###
                #Random BIOS error
                if self.AlertCounter['BIOS NOT WORKING'] == 0:
                    error = round(random(), 2)
                    if error > 0.99:
                        self.AlertCounter['BIOS NOT WORKING'] += 1
                        self.power = 0.0
                ###
            elif self.name == 'CHIPSET':
                ###
                #Chipset output error
                if self.chipset_power <= 30.0 and self.AlertCounter['LOW CHIPSET OUTPUT'] == 0:
                    self.AlertCounter['LOW CHIPSET OUTPUT'] += 1
                elif self.chipset_power > 30.0 and self.AlertCounter['LOW CHIPSET OUTPUT'] == 1:
                    self.AlertCounter['LOW CHIPSET OUTPUT'] -= 1
                ###
                #Temperature error
                if self.temperature >= 55.0 and self.AlertCounter['HIGH TEMPERATURE'] == 0:
                    self.AlertCounter['HIGH TEMPERATURE'] += 1
                elif self.temperature < 55.0 and self.AlertCounter['HIGH TEMPERATURE'] == 1:
                    self.AlertCounter['HIGH TEMPERATURE'] -= 1
                ###
                #Power error
                if self.power <= 21.38 and self.AlertCounter['LOW POWER'] == 0:
                    self.AlertCounter['LOW POWER'] += 1
                elif self.power > 21.38 and self.AlertCounter['LOW POWER'] == 1:
                    self.AlertCounter['LOW POWER'] -= 1
                ###
            elif self.name == 'GPU':
                ###
                #Random increase of graphics usage between 0% and 10%
                self.generate_resource()
                ###
                #Graphics errors
                if self.graphics >= 0.8 and self.AlertCounter['TOO MUCH GRAPHICS'] == 0:    #Activates the too much graphic usage alert
                    self.AlertCounter['TOO MUCH GRAPHICS'] += 1
                elif self.graphics < 0.8 and self.AlertCounter['TOO MUCH GRAPHICS'] == 1:   #Deactivates the too much graphic usage alert
                    self.AlertCounter['TOO MUCH GRAPHICS'] -= 1

                if self.graphics > 0.65 and self.AlertCounter['GRAPHICS NOT WORKING'] == 0: #Activates with a 15% chance the graphics not working error if graphic usage abive 65%
                    error = round(random(), 2)
                    if error > 0.85:    #15% chance for the error to trigger
                        self.AlertCounter['GRAPHICS NOT WORKING'] += 1
                        self.CustomAlertPercentage += 100
                        self.graphics = 0.0
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
                ###
            elif self.name == 'VENT':
                ###
                #Decrease of rpm
                if self.rpm > 0:
                    self.rpm -= 15.0*self.VentNum
                    if self.rpm < 0:
                        self.rpm = 0
                ###
                #Vent error
                if self.VentNum > 0:    #A vent error can happen only if there is at least 1 vent working
                    error = round(random(), 2)
                    if error > 0.95:    #5% chance for the error to trigger
                        self.AlertCounter['VENT NOT WORKING'] +=1
                        self.VentNum -= 1.0
                        self.CustomAlertPercentage += 100
                ###
                #Temperature error
                if self.temperature >= -10.0 and self.AlertCounter['HIGH TEMPERATURE'] == 0:
                    self.AlertCounter['HIGH TEMPERATURE'] += 1
                elif self.temperature < -10.0 and self.AlertCounter['HIGH TEMPERATURE'] ==1:
                    self.AlertCounter['HIGH TEMPERATURE'] -=1
                ###
                #Power error
                if self.power <= 22.5 and self.AlertCounter['LOW POWER'] == 0:
                    self.AlertCounter['LOW POWER'] += 1
                elif self.power > 22.5 and self.AlertCounter['LOW POWER'] == 1:
                    self.AlertCounter['LOW POWER'] -= 1
                ###
        else:
            pass

    def custom_alert(self, bit): #Method that fixes the alerts that are not value dependant
        if self.functional:
            if self.name == 'PERI':
                if self.AlertCounter['PERIPHERAL NOT WORKING'] > 0 and bit.subsystem:
                    self.CustomAlertPercentage -= randrange(0, 4)
                    if self.CustomAlertPercentage < 0:
                        self.CustomAlertPercentage = 0
                    if self.CustomAlertPercentage <= 300 and self.AlertCounter['PERIPHERAL NOT WORKING'] == 4:
                        self.AlertCounter['PERIPHERAL NOT WORKING'] -= 1
                        self.PeriNum += 1.0
                    elif self.CustomAlertPercentage == 0 and self.AlertCounter['VENT NOT WORKING'] == 3:
                        self.AlertCounter['PERIPHERAL NOT WORKING'] -= 1
                        self.PeriNum += 1.0
                    elif self.CustomAlertPercentage <= 100 and self.AlertCounter['VENT NOT WORKING'] == 2:
                        self.AlertCounter['PERIPHERAL NOT WORKING'] -= 1
                        self.PeriNum += 1.0
                    elif self.CustomAlertPercentage == 0 and self.AlertCounter['VENT NOT WORKING'] == 1:
                        self.AlertCounter['PERIPHERAL NOT WORKING'] -= 1
                        self.PeriNum += 1.0
                        bit.subsystem = False
                        bit.FixCheck = False
                elif self.AlertCounter['VENT NOT WORKING'] == 0 and bit.subsystem:
                    bit.subsystem = False
                    bit.FixCheck = False
            elif self.name == 'VRM':
                if self.AlertCounter['VRM NOT WORKING'] == 1 and bit.subsystem:
                    self.CustomAlertPercentage -= randrange(0, 4)
                    if self.CustomAlertPercentage < 0:
                        self.CustomAlertPercentage = 0
                    if self.CustomAlertPercentage == 0:  # If there is no more error to be fixed, it gets deleted and the bit exits the subsystem
                        self.AlertCounter['VRM NOT WORKING'] -= 1
                        bit.subsystem = False
                        bit.FixCheck = False
                elif self.AlertCounter['VRM NOT WORKING'] == 0 and bit.subsystem:  # In case there were more than one bit working to fix the error and it is already fixed, they get dismissed from the task
                    bit.subsystem = False
                    bit.FixCheck = False
            elif self.name == 'RAM':    #Does not have custom alert
                if bit.subsystem:
                    bit.subsystem = False
                    bit.FixCheck = False
            elif self.name == 'ATX':    #Does not have custom alert
                if bit.subsystem:
                    bit.subsystem = False
                    bit.FixCheck = False
            elif self.name == 'CPU':    #Does not have custom alert
                if bit.subsystem:
                    bit.subsystem = False
                    bit.FixCheck = False
            elif self.name == 'DISK':
                pass
            elif self.name == 'CLK':
                pass
            elif self.name == 'BIOS':
                if self.AlertCounter['BIOS NOT WORKING'] == 1 and bit.subsystem:
                    self.CustomAlertPercentage -= randrange(0, 4)
                    if self.CustomAlertPercentage < 0:
                        self.CustomAlertPercentage = 0
                    if self.CustomAlertPercentage == 0:  # If there is no more error to be fixed, it gets deleted and the bit exits the subsystem
                        self.AlertCounter['BIOS NOT WORKING'] -= 1
                        bit.subsystem = False
                        bit.FixCheck = False
                elif self.AlertCounter['BIOS NOT WORKING'] == 0 and bit.subsystem:  # In case there were more than one bit working to fix the error and it is already fixed, they get dismissed from the task
                    bit.subsystem = False
                    bit.FixCheck = False
            elif self.name == 'CHIPSET':    #Does not have custom alert
                if bit.subsystem:
                    bit.subsystem = False
                    bit.FixCheck = False
            elif self.name == 'GPU':
                if self.AlertCounter['GRAPHICS NOT WORKING'] == 1 and bit.subsystem:  #If there is an error it starts fixing it
                    self.CustomAlertPercentage -= randrange(0, 4)   #Decreases the percentage of error left to fix in a random from 1 to 3
                    if self.CustomAlertPercentage < 0:
                        self.CustomAlertPercentage = 0
                    if self.CustomAlertPercentage == 0: #If there is no more error to be fixed, it gets deleted and the bit exits the subsystem
                        self.AlertCounter['GRAPHICS NOT WORKING'] -= 1
                        bit.subsystem = False
                        bit.FixCheck = False
                elif self.AlertCounter['GRAPHICS NOT WORKING'] == 0 and bit.subsystem: #In case there were more than one bit working to fix the error and it is already fixed, they get dismissed from the task
                    bit.subsystem = False
                    bit.FixCheck = False
                else:   #If there is no active error it raises an error
                    raise InvalidFix('NO ERROR TO BE FIXED IN THIS LOCATION')
            elif self.name == 'VENT':
                if self.AlertCounter['VENT NOT WORKING'] > 0 and bit.subsystem:
                    self.CustomAlertPercentage -= randrange(0, 4)
                    if self.CustomAlertPercentage < 0:
                        self.CustomAlertPercentage = 0
                    if self.CustomAlertPercentage <= 200 and self.AlertCounter['VENT NOT WORKING'] == 3:
                        self.AlertCounter['VENT NOT WORKING'] -= 1
                        self.VentNum += 1.0
                    elif self.CustomAlertPercentage <= 100 and self.AlertCounter['VENT NOT WORKING'] == 2:
                        self.AlertCounter['VENT NOT WORKING'] -= 1
                        self.VentNum += 1.0
                    elif self.CustomAlertPercentage == 0 and self.AlertCounter['VENT NOT WORKING'] == 1:
                        self.AlertCounter['VENT NOT WORKING'] -= 1
                        self.VentNum += 1.0
                        bit.subsystem = False
                        bit.FixCheck = False
                elif self.AlertCounter['VENT NOT WORKING'] == 0 and bit.subsystem:
                    bit.subsystem = False
                    bit.FixCheck = False
        else:
            bit.subsystem = False
            bit.FixCheck = False
            raise FunctionalityError('CANT FIX SOMETHING THAT IS NOT WORKING')

    def temp_increase(self): #Method to calculate how much temperature does the location have
        if self.functional:
            if self.name == 'PERI':
                if CHIPSET.chipset_power > 0.0:
                    if self.temperature < 5.0*self.PeriNum:
                        self.temperature += 0.2
                else:
                    self.temperature = 10.0*self.PeriNum
            elif self.name == 'VRM':
                if self.refined_power <= 100.0 and self.temperature < 60.0:
                    self.temperature += 1.0
                elif self.refined_power > 100.0:
                    self.temperature = 10.0*(6.0*(self.refined_power/1000.0)) + 60.0
            elif self.name == 'RAM':
                if self.ram_in_use <= 2.0 and self.temperature < 40.0:
                    self.temperature += 1.0
                elif self.ram_in_use > 2.0:
                    self.temperature = self.consumption*(5.125*(self.ram_in_use/10)) + 40
            elif self.name == 'ATX':    #Does not generate temperature
                pass
            elif self.name == 'CPU':
                if self.processes <= 20.0 and self.temperature < 30.0:
                    self.temperature += 1.0
                elif self.processes > 20.0:
                    self.temperature = self.consumption*(1*(self.processes/100)) + 30
            elif self.name == 'DISK':
                pass
            elif self.name == 'CLK':
                pass
            elif self.name == 'BIOS':
                self.temperature = self.power*0.1
            elif self.name == 'CHIPSET':
                if self.chipset_power <= 40.0:
                    self.temperature += 1.0
                else:
                    self.temperature = self.consumption*((self.chipset_power/100.0) + 1.59) + 30.0
            elif self.name == 'GPU':
                if self.graphics <= 0.89:
                    if self.temperature < 75.0:
                        self.temperature += 1.0
                else:
                    self.temperature = self.consumption*(self.graphics - 0.89) + 75.0
            elif self.name == 'VENT':
                if self.rpm <= 2400.0:
                    if self.temperature > -30.0:
                        self.temperature -= 1.0
                else:
                    self.temperature = -(self.consumption*(3.6 + self.rpm) + 30.0)
        else:
            pass

    def power_management(self):    #Method to calculate how much power the location has each second
        if self.name == 'PERI':
            if self.power >= self.consumption*self.PeriNum:
                if not self.functional:
                    self.functional = True
                variable_consumption = (1.0 - (CHIPSET.chipset_power/100))
                if variable_consumption < 0:
                    variable_consumption = 0
                self.power -= (self.consumption*variable_consumption)*self.PeriNum + self.consumption*self.PeriNum
            else:
                self.reset_location()
        elif self.name == 'VRM':
            if self.temperature < 120.0:
                if not self.functional:
                    self.functional = True
            else:
                self.reset_location()
        elif self.name == 'RAM':
            if self.power >= self.consumption and self.temperature < 81.0:
                if not self.functional:
                    self.functional = True
                self.power -= self.consumption
            else:
                self.reset_location()
        elif self.name == 'ATX':    #Does not consume power, it generates it
            if self.stored_power > 4500.0:
                self.reset_location()
        elif self.name == 'CPU':
            if self.refined_power >= self.consumption and self.temperature <50.0:
                if not self.functional:
                    self.functional = True
                self.refined_power -= self.consumption
            else:
                self.functional = True
        elif self.name == 'DISK':
            pass
        elif self.name == 'CLK':
            pass
        elif self.name == 'BIOS':   #Does not naturally consume power
            pass
        elif self.name == 'CHIPSET':
            if self.power >= self.consumption and self.temperature <= 65.0:
                if not self.functional:
                    self.functional = True
                variable_consumption = (self.chipset_power/100) - 1.5
                if  variable_consumption < 0:
                    variable_consumption = 0
                self.power -= self.consumption*variable_consumption + self.consumption
            else:
                self.reset_location()
        elif self.name == 'GPU':
            if self.power >= self.consumption:
                if not self.functional:
                    self.functional = True
                variable_consumption = self.graphics - 0.9
                if variable_consumption < 0:
                    variable_consumption = 0
                self.power -= self.consumption*variable_consumption + self.consumption
                if self.power < 0:
                    self.power = 0
            else:
                self.reset_location()
        elif self.name == 'VENT':
            if self.power >= self.consumption*self.VentNum:
                if not self.functional:
                    self.functional = True
                variable_consumption = (self.rpm/1000) - 2.4
                if variable_consumption < 0:
                    variable_consumption = 0
                self.power -= self.consumption*variable_consumption + self.consumption*self.VentNum
                if self.power < 0:
                    self.power = 0
            else:
                self.reset_location()

    def generate_resource(self):    #Method that generates the 'resources' of each specific location
        if self.functional:
            if self.name == 'PERI':
                CHIPSET.chipset_power -= round(uniform(0.0, 2.0), 2)*self.PeriNum
            elif self.name == 'VRM':
                if self.power >= 100.0:
                    self.power -= 100; self.refined_power += 10
            elif self.name == 'RAM':
                ram_change = round(uniform(0.0, 0.5), 3)
                self.ram_in_use += ram_change
                self.available_ram -= ram_change
            elif self.name == 'ATX':
                self.stored_power += round(uniform(10.0, 15.0), 2)
            elif self.name == 'CPU':
                self.processes += randrange(1, 6)
            elif self.name == 'DISK':
                pass
            elif self.name == 'CLK':
                pass
            elif self.name == 'BIOS':   #Uses power to build bits
                self.power -= 1
                self.BitBuilding += round(uniform(0.0, 2.5), 2)
                if self.BitBuilding >= 100.0:
                    self.BitBuilding = 0.0
                    if ModelBit.counter == 64:
                        ModelBit.counter = 0
                    bit_name = str(ModelBit.counter + 1)
                    new_bit = 'Bit'+bit_name+'=ModelBit('+bit_name+'locations)' #Hace falta revisar esto cuando se tenga la version final
                    exec(new_bit)
            elif self.name == 'CHIPSET':
                self.chipset_power += round(uniform(0.0, 3.0), 2)
            elif self.name == 'GPU':
                if self.AlertCounter['GRAPHICS NOT WORKING'] == 0: #Graphics only increase if working
                    if self.graphics < 1:
                        self.graphics += round(uniform(0.0, 0.1), 2)
                        if self.graphics >= 1:
                            self.graphics += round(uniform(0.0, 0.03), 2)    #Graphic usage rises slower because it will generate too much heat, aka, temperature error
            elif self.name == 'VENT':
                if self.rpm < 2400.0:
                    self.rpm += 50*self.VentNum
                else:
                    self.rpm += 10*self.VentNum
                if self.rpm > 3000.0:
                    self.rpm = 3000.0
        else:
            pass

    def get_mined(self, bit):    #Method for when it is mined by a bit
        if self.functional:
            if self.name == 'PERI':
                raise MiningError('PERIPHERALS CANT BE MINED')
            elif self.name == 'VRM':
                self.generate_resource()
            elif self.name == 'RAM':
                ram_change = round(uniform(0.0, 0.1), 3)
                self.ram_in_use -= ram_change
                self.available_ram += ram_change
            elif self.name == 'ATX':
                self.generate_resource()
            elif self.name == 'CPU':
                self.processes -= randrange(1, 3)
            elif self.name == 'DISK':
                pass
            elif self.name == 'CLK':
                pass
            elif self.name == 'BIOS':
                if self.AlertCounter['BIOS NOT WORKING'] == 0 and self.power > 0:
                    self.generate_resource()
                else:
                    raise MiningError('MINING IS NOT POSSIBLE IN BIOS RIGHT NOW')
            elif self.name == 'CHIPSET':
                self.generate_resource()
            elif self.name == 'GPU':    #In GPU case, its graphic usage must be reduced
                if self.AlertCounter['GRAPHICS NOT WORKING'] == 0:
                    self.graphics -= round(uniform(0.005, 0.03), 2)
                else:
                    raise MiningError('MINING IS NOT POSSIBLE IN GPU RIGHT NOW')
            elif self.name == 'VENT':
                if self.VentNum != 0:
                    self.generate_resource()
                else:
                    raise MiningError('MINING IS NOT POSSIBLE IN GPU RIGHT NOW')
        else:
            raise FunctionalityError('CANT MINE IT WHEN IT IS NOT WORKING')

    def get_power(self, bit):    #Method for when a bit gives power to a location
        charge = bit.load
        self.power += charge
        bit.load = 0

    def give_power(self, bit):  #Method for when a bit gets power from a location
        charge = bit.limit - bit.load
        self.power -= charge
        bit.load += charge