from Imports import *

class Settings:
    value = 0
    def __init__(self):
        self.volume = 60
        self.window_width = WIDTH
        self.window_height = HEIGHT
        self.fps = 60

    def set_volume(self, volume):
        self.volume = volume

    def set_resolution(self, WIDTH):
        self.window_width = WIDTH
        self.window_height = WIDTH * 0.755

    def set_fps(self,fps):          # TODO aplicar en el main -> clock.tick(fps)
        self.fps = fps

    def apply_settings(self):
        pygame.mixer.music.set_volume(self.volume)
        return (self.window_width, self.window_height)

# Cambiando settings
settings = Settings()
volum = settings.set_volume(50)
resolution = settings.set_resolution(1250)
fps = settings.set_fps(75)
settings.apply_settings()

pygame.quit()