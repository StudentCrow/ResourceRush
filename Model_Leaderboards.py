import pygame
import sys
from Resources import *
from Viewer_Menu import *
from Viewer_Leaderboards import *

pygame.init()

class Leaderboards: # TODO singular
    def __init__(self):
        self.scores = []        # creo vector scores vacío
        self.names = []

    def set_scores(self, score):
        self.scores.append(score)    # agrego puntuación al vector scores

    def sort_scores(self):
        self.scores.sort(reverse=True)      # ordeno de mayor a menor

    def print_scores(self, num_scores=5):
        top_scores = self.scores[:num_scores]       # asigno al vector los primeros 5 valores
        print(top_scores)

    def set_names(self, name):
        self.names.append(name)         # añado un nombre al vector

#    def assign_names(self, top_score):




# ejemplo
Leaderboards = Leaderboards()       # llamo a mi clase Leaderboards
Leaderboards.set_scores(500)        # setteo valores
Leaderboards.set_scores(800)
Leaderboards.set_scores(300)
Leaderboards.set_scores(1200)
Leaderboards.set_scores(1300)
Leaderboards.set_scores(1400)
Leaderboards.set_scores(1500)
Leaderboards.set_scores(104)
Leaderboards.set_scores(1030)
Leaderboards.set_scores(789)

Leaderboards.sort_scores()          # ordeno de mayor a menor
Leaderboards.print_scores()         # imprimo valores top

pygame.quit()