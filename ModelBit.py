import pygame
import ModelOrder

class ModelBit:
    """
    Model part class that controls each individual bit
    """
    def __init__(self, time = 0.0, working = False, subsystem = False, critic = False):
        self.time = time    #Determines the remining lifetime of the bit
        self.working = working  #Boolean that indicates if the bit is currently working or in standby
        self.subsystem = subsystem  #Boolean that indicates if the bit is working in a subsystem or not
        self.critic = critic    #Boolean that indicates if the bit is in critic state or not
        self.loc = 'BIOS'   #Location where the bit is currently positionated