# pygame.image.load(imagen) -> carga imagen
# .blit(imagen , (x, y)) -> dibuja imagen en coordenadas (x, y)
import sys
import pygame

pygame.init()

WIDTH = 1000
HEIGHT = 725

def main():
    # creación ventana y título
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Resource Rush")
    # cargar fondo e imagen
    img_background = pygame.image.load("img/ResourceRushMenu.png").convert()
    img_new_mission = pygame.image.load("img/NewMission.jpeg").convert_alpha()
    img_continue_mission = pygame.image.load("img/ContinueMission.jpeg").convert_alpha()
    img_settings = pygame.image.load("img/Settings.jpeg").convert_alpha()
    img_leaderboards = pygame.image.load("img/Leaderboards.jpeg").convert_alpha()
    img_quit_game = pygame.image.load("img/QuitGame.jpeg").convert_alpha()
    # posición de las imágenes en window
    window.blit(img_background, (0, 0))
    window.blit(img_new_mission, (0.34 * WIDTH, 0.42 * HEIGHT))
    window.blit(img_continue_mission, (0.325 * WIDTH, 0.525 * HEIGHT))
    window.blit(img_settings, (0.365 * WIDTH, 0.62 * HEIGHT))
    window.blit(img_leaderboards, (0.33 * WIDTH, 0.75 * HEIGHT))
    window.blit(img_quit_game, (0.34 * WIDTH, 0.845 * HEIGHT))
    # se muestran los cambios en la pantalla
    pygame.display.flip()
    # bucle principal
    while True:
        #posibles entradas del teclado y ratón
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

if __name__ == "__main__":
    main()

# --------------------------------------------------------------
# PARA DIMENSIONAR LAS IMÁGENES A LA RESOLUCIÓN:
# 2 Modificar superficie para el fondo de la window
# background_surface = pygame.Surface((WIDTH, HEIGHT))
# 3 Meter if en el while del bucle del main model
#    if WIDTH != 1000 or HEIGHT != 725:
#        background_surface = pygame.Surface((WIDTH, HEIGHT))
#        background_surface.blit(pygame.transform.scale(img_background, (WIDTH, HEIGHT)), (0, 0))

pygame.quit()