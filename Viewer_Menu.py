from Imports import *
from Viewer_Settings import *
pygame.init()
def Menu():
    # creación ventana y título
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Resource Rush")
    # fuente texto
    font = pygame.font.SysFont("Showcard Gothic", 45)
    # cargar fondo e imagen
    img_background = pygame.image.load("img/ResourceRushMenu.png")
    new_mission_text = font.render("New Mission", True, BLUE)
    practice_text = font.render("Practice", True, PURPLE)
    settings_text = font.render("Settings", True, GREEN)
    leaderboards_text = font.render("Leaderboards", True, ORANGE)
    quit_game_text = font.render("Quit Game", True, RED)

    new_mission_rect_coord = new_mission_text.get_rect(center=(WIDTH / 2, 0.45 * HEIGHT))
    practice_rect_coord = practice_text.get_rect(center=(WIDTH / 2, 0.57 * HEIGHT))
    settings_rect_coord = settings_text.get_rect(center=(WIDTH / 2, 0.69 * HEIGHT))
    leaderboards_rect_coord = leaderboards_text.get_rect(center=(WIDTH / 2, 0.82 * HEIGHT))
    quit_game_rect_coord = quit_game_text.get_rect(center=(WIDTH / 2, 0.94 * HEIGHT))

    window.blit(img_background, (0, 0))
    pygame.draw.rect(window, WHITE, new_mission_rect_coord)
    pygame.draw.rect(window, WHITE, practice_rect_coord)
    pygame.draw.rect(window, WHITE, settings_rect_coord)
    pygame.draw.rect(window, WHITE, leaderboards_rect_coord)
    pygame.draw.rect(window, WHITE, quit_game_rect_coord)
    window.blit(new_mission_text, new_mission_rect_coord)
    window.blit(practice_text, practice_rect_coord)
    window.blit(settings_text, settings_rect_coord)
    window.blit(leaderboards_text, leaderboards_rect_coord)
    window.blit(quit_game_text, quit_game_rect_coord)

    pygame.display.flip()

    # BUCLE
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if new_mission_rect_coord.collidepoint(event.pos):
                    print("Empezamos misión wachín.")
                elif practice_rect_coord.collidepoint(event.pos):
                    print("Continuamos misión wacho.")
                elif settings_rect_coord.collidepoint(event.pos):
                    print("Vas a bajarle la dificultad? Haha, cobarde.")
                elif leaderboards_rect_coord.collidepoint(event.pos):
                    print("Mejor ni lo mires, que eres el último.")
                elif quit_game_rect_coord.collidepoint(event.pos):
                    running = False
                    sys.exit()

pygame.quit()