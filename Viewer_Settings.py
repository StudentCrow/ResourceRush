from Imports import *
def Settings():
    # Ventana
    window = pygame.display.set_mode(WINDOW_DIM)
    pygame.display.set_caption("SETTINGS")
    # Administrador de interfaz
    manager = pygame_gui.UIManager(WINDOW_DIM)
    # Sonidos
    sound1 = pygame.mixer.Sound("sounds/fps.mp3")
    sound2 = pygame.mixer.Sound("sounds/volume.mp3")
    sound3 = pygame.mixer.Sound("sounds/resolution.mp3")
    # Fuente y títulos
    font = pygame.font.SysFont("Showcard Gothic", 45)
    font2 = pygame.font.SysFont("Showcard Gothic", 26)
    settings_text = font.render("SETTINGS", True, GREEN)
    title_fps = font.render("Fps", True, BLUE)
    subtitle_fps = font2.render("30/60/90/120", True, BLUE)
    title_volume = font.render("Volume", True, BLUE)
    subtitle_volume = font2.render("ON/OFF", True, BLUE)
    title_resolution = font.render("Resolution", True, BLUE)
    subtitle_resolution = font2.render("900x680 or 1000x755", True, BLUE)

    # Cuadros de texto
    text_entry_fps = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((WIDTH / 10, 0.57 * HEIGHT), (200, 50)))
    text_entry_volume = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((7 * WIDTH / 10, 0.57 * HEIGHT), (200, 50)))
    text_entry_resolution = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((WIDTH / 2.5, 0.77 * HEIGHT), (200, 50)))

    # Restricciones de texto
    text_entry_fps.set_allowed_characters(numb)
    text_entry_fps.set_text_length_limit(3)
    text_entry_volume.set_allowed_characters(numb)
    text_entry_volume.set_text_length_limit(3)
    text_entry_resolution.set_allowed_characters(numb)
    text_entry_resolution.set_text_length_limit(8)

    # coordenadas de títulos
    settings_text_rect_coord = settings_text.get_rect(center=(WIDTH / 2, 0.3 * HEIGHT))
    title_fps_rect_coord = title_fps.get_rect(center=(WIDTH / 5, 0.5 * HEIGHT))
    subtitle_fps_rect_coord = subtitle_fps.get_rect(center=(WIDTH / 5, 0.55 * HEIGHT))
    title_volume_rect_coord = title_volume.get_rect(center=(4 * WIDTH / 5, 0.5 * HEIGHT))
    subtitle_volume_rect_coord = subtitle_volume.get_rect(center=(4 * WIDTH / 5, 0.55 * HEIGHT))
    title_resolution_rect_coord = title_resolution.get_rect(center=(WIDTH / 2, 0.7 * HEIGHT))
    subtitle_resolution_rect_coord = subtitle_resolution.get_rect(center=(WIDTH / 2, 0.75 * HEIGHT))

    running = True
    clock = pygame.time.Clock()
    while running:
        time_delta = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if text_entry_fps.is_focused:
                    if event.key == pygame.K_RETURN:
                        text = text_entry_fps.get_text()
                        if text == "30" or "60" or "90" or "120":
                            sound1.play()
                            text_entry_fps.set_text("")
                if text_entry_volume.is_focused:
                    if event.key == pygame.K_RETURN:
                        text = text_entry_volume.get_text()
                        if text == "10" or "20" or "30" or "40" or "50" or "60" or "70" or "80" or "90" or "100":
                            sound3.play()
                            text_entry_volume.set_text("")
                if text_entry_resolution.is_focused:
                    if event.key == pygame.K_RETURN:
                        text = text_entry_resolution.get_text()
                        if text == "1800x755" or "900x680":
                            sound2.play()
                            text_entry_resolution.set_text("")
            manager.process_events(event)
        manager.update(time_delta)

        window.fill(BLACK)

        pygame.draw.rect(window, BLACK, settings_text_rect_coord)
        pygame.draw.rect(window, BLACK, title_fps_rect_coord)
        pygame.draw.rect(window, BLACK, subtitle_fps_rect_coord)
        pygame.draw.rect(window, BLACK, title_volume_rect_coord)
        pygame.draw.rect(window, BLACK, subtitle_volume_rect_coord)
        pygame.draw.rect(window, BLACK, title_resolution_rect_coord)
        pygame.draw.rect(window, BLACK, subtitle_resolution_rect_coord)

        window.blit(settings_text, settings_text_rect_coord)
        window.blit(title_fps, title_fps_rect_coord)
        window.blit(subtitle_fps, subtitle_fps_rect_coord)
        window.blit(title_volume, title_volume_rect_coord)
        window.blit(subtitle_volume, subtitle_volume_rect_coord)
        window.blit(title_resolution, title_resolution_rect_coord)
        window.blit(subtitle_resolution, subtitle_resolution_rect_coord)

        manager.draw_ui(window)

        pygame.display.update()

Settings()

pygame.quit()