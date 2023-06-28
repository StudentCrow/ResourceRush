import pygame


class ModelClock:
    clock_counter = 0

    def __init__(self,  timer):
        self.timer = timer
        ModelClock.clock_counter += 1

    def createClock(self):
        timer_event = pygame.USEREVENT + ModelClock.clock_counter
        clock_timer = pygame.time.set_timer(timer_event, self.timer)
        return timer_event, clock_timer