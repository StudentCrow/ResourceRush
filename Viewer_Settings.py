from Imports import *
def Settings():
    # Ventana
    window = pygame.display.set_mode(WINDOW_DIM)
    pygame.display.set_caption("SETTINGS")
    # Fuente y títulos
    font = pygame.font.SysFont("Showcard Gothic", 45)
    settings_text = font.render("SETTINGS", True, GREEN)
    title_fps = font.render("Fps", True, BLUE)
    title_volume = font.render("Volume", True, BLUE)
    title_resolution = font.render("Resolution", True, BLUE)

    # coordenadas de títulos
    settings_text_rect_coord = settings_text.get_rect(center=(WIDTH / 2, 0.3 * HEIGHT))
    title_fps_rect_coord = title_fps.get_rect(center=(WIDTH / 5, 0.5 * HEIGHT))
    title_volume_rect_coord = title_volume.get_rect(center=(4 * WIDTH / 5, 0.5 * HEIGHT))
    title_resolution_rect_coord = title_resolution.get_rect(center=(WIDTH / 2, 0.3 * HEIGHT))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        window.fill(BLACK)

        pygame.draw.rect(window, BLACK, settings_text_rect_coord)
        pygame.draw.rect(window, BLACK, title_fps_rect_coord)
        pygame.draw.rect(window, BLACK, title_volume_rect_coord)
        pygame.draw.rect(window, BLACK, title_resolution_rect_coord)

        window.blit(settings_text, settings_text_rect_coord)
        window.blit(title_fps, title_fps_rect_coord)
        window.blit(title_volume, title_volume_rect_coord)
        window.blit(title_resolution, title_resolution_rect_coord)

        pygame.display.update()

Settings()
pygame.quit()