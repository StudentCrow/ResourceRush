import pygame


class ViewClock:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0
        self.hours = 0
        self.color = (0, 0, 0)
        self.font = pygame.font.SysFont('arial', 20)

    def drawClock(self, screen):
        time = str(self.hours)+':'+str(self.minutes)+':'+str(self.seconds)
        text_image = self.font.render(time, True, self.color)
        text_rect = text_image.get_rect(topleft=screen.get_rect().topleft)
        screen.blit(text_image, text_rect)