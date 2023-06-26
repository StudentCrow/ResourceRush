from Imports import *
def NewMission():
    # Ventana
    window = pygame.display.set_mode(WINDOW_DIM)
    pygame.display.set_caption("New Mission")
    # Administrador de interfaz
    manager = pygame_gui.UIManager(WINDOW_DIM)
    # Fuente y título de texto
    font = pygame.font.SysFont("Showcard Gothic", 45)
    title_text = font.render("Introduzca su nombre", True, RED)
    title_rect_coord = title_text.get_rect(center=(WIDTH / 2, 0.3 * HEIGHT))
    # Cuadro de texto
    text_entry = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((0.35 * WIDTH, 0.4 * HEIGHT), (0.3 * WIDTH, 0.08 * HEIGHT)),
        manager=manager,
        visible=True)
    text_entry.set_allowed_characters(abc)
    text_entry.set_text_length_limit(3)
    # Bucle principal -----------------------------------------------------------
    running = True
    clock = pygame.time.Clock()
    while running:
        time_delta = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    print("Ir hacia interfaz de juego")
            manager.process_events(event)
        manager.update(time_delta)
        window.fill(BLACK)
        pygame.draw.rect(window, BLACK, title_rect_coord)
        window.blit(title_text, title_rect_coord)
        manager.draw_ui(window)
        pygame.display.update()


pygame.quit()