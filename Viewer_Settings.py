from Imports import *
def Settings():
    # Ventana
    window = pygame.display.set_mode(WINDOW_DIM)
    pygame.display.set_caption("SETTINGS")
    # Fuente y títulos
    font = pygame.font.SysFont("Showcard Gothic", 45)
    title_text = font.render("SETTINGS", True, GREEN)
    title_rect_coord = title_text.get_rect(center=(WIDTH / 2, 0.3 * HEIGHT))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        window.fill(BLACK)
        pygame.draw.rect(window, BLACK, title_rect_coord)
        window.blit(title_text, title_rect_coord)
        pygame.display.update()

pygame.quit()