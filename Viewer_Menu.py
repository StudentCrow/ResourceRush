import pygame, sys
from Colors import *
pygame.init()

WIDTH = 1000
HEIGHT = 755

def menu():
    # creación ventana y título
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Resource Rush")
    # fuente texto
    font = pygame.font.SysFont("Showcard Gothic", 45)
    # cargar fondo e imagen
    img_background = pygame.image.load("img/ResourceRushMenu.png")
    new_mission_text = font.render("New Mission", True, BLUE)
    continue_mission_text = font.render("Continue Mission", True, PURPLE)
    settings_text = font.render("Settings", True, GREEN)
    leaderboards_text = font.render("Leaderboards", True, ORANGE)
    quit_game_text = font.render("Quit Game", True, RED)

    new_mission_rect_coord = new_mission_text.get_rect(center=(WIDTH / 2, 0.45 * HEIGHT))
    continue_mission_rect_coord = continue_mission_text.get_rect(center=(WIDTH / 2, 0.57 * HEIGHT))
    settings_rect_coord = settings_text.get_rect(center=(WIDTH / 2, 0.69 * HEIGHT))
    leaderboards_rect_coord = leaderboards_text.get_rect(center=(WIDTH / 2, 0.82 * HEIGHT))
    quit_game_rect_coord = quit_game_text.get_rect(center=(WIDTH / 2, 0.94 * HEIGHT))

    window.blit(img_background, (0, 0))
    pygame.draw.rect(window, WHITE, new_mission_rect_coord)
    pygame.draw.rect(window, WHITE, continue_mission_rect_coord)
    pygame.draw.rect(window, WHITE, settings_rect_coord)
    pygame.draw.rect(window, WHITE, leaderboards_rect_coord)
    pygame.draw.rect(window, WHITE, quit_game_rect_coord)
    window.blit(new_mission_text, new_mission_rect_coord)
    window.blit(continue_mission_text, continue_mission_rect_coord)
    window.blit(settings_text, settings_rect_coord)
    window.blit(leaderboards_text, leaderboards_rect_coord)
    window.blit(quit_game_text, quit_game_rect_coord)

    pygame.display.flip()

    # BUCLE MAIN
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if new_mission_rect_coord.collidepoint(
                        event.pos):
                    print("Empezamos misión wachín.")  # TODO acción a cambiar
                elif continue_mission_rect_coord.collidepoint(event.pos):
                    print("Continuamos misión wacho.")  # TODO acción a cambiar
                elif settings_rect_coord.collidepoint(event.pos):
                    print("Vas a bajarle la dificultad? Haha, cobarde.")  # TODO acción a cambiar
                elif leaderboards_rect_coord.collidepoint(event.pos):
                    print("Mejor ni lo mires, que eres el último.")  # TODO acción a cambiar
                elif quit_game_rect_coord.collidepoint(event.pos):  # si se clica en el botón QUIT GAME
                    running = False


if __name__ == "__main__":
    menu()

pygame.quit()