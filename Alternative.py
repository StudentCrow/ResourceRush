from Imports import *
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
                    NewMission()
                elif practice_rect_coord.collidepoint(event.pos):
                    print("Continuamos misión wacho.")
                    # TODO crear practice
                elif settings_rect_coord.collidepoint(event.pos):
                    print("Vas a bajarle la dificultad? Haha, cobarde.")
                    Settings()
                elif leaderboards_rect_coord.collidepoint(event.pos):
                    print("Mejor ni lo mires, que eres el último.")
                    Leaderboards()
                elif quit_game_rect_coord.collidepoint(event.pos):
                    running = False
                    sys.exit()

def NewMission():       # TODO falta boton para atrás
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
                    print("Ir hacia interfaz de juego") # TODO falta unión con la interfaz principal de juego

            manager.process_events(event)
        manager.update(time_delta)
        window.fill(BLACK)
        pygame.draw.rect(window, BLACK, title_rect_coord)
        window.blit(title_text, title_rect_coord)
        manager.draw_ui(window)
        pygame.display.update()

def Leaderboards():
    # creación ventana, título y background
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Leaderboards")
    img_background = pygame.image.load("img/Leaderboards.png")
    # fuente texto
    font = pygame.font.SysFont("Showcard Gothic", 45)
    # dibujar el background
    window.blit(img_background, (0, 0))

# -------------------------------------------------------------------------------------- TÍTULOS RANK, SCORE, NAME
    # rank, score, name
    rank_text = font.render("Rank", True, WHITE)
    score_text = font.render("Score", True, WHITE)
    name_text = font.render("Name", True, WHITE)
    # coordenadas de texto
    rank_coord_rect = rank_text.get_rect(center=(3 * WIDTH / 10, 0.3 * HEIGHT))
    score_coord_rect = score_text.get_rect(center=(5 * WIDTH / 10, 0.3 * HEIGHT))
    name_coord_rect = name_text.get_rect(center=(7 * WIDTH / 10, 0.3 * HEIGHT))
    # dibujo texto
    window.blit(rank_text, rank_coord_rect)
    window.blit(score_text, score_coord_rect)
    window.blit(name_text, name_coord_rect)

# ---------------------------------------------------------------------------------- COLUMNA RANKS
    # ranks
    rank1_text = font.render("1ST", True, WHITE)
    rank2_text = font.render("2ND", True, WHITE)
    rank3_text = font.render("3RD", True, WHITE)
    rank4_text = font.render("4TH", True, WHITE)
    rank5_text = font.render("5TH", True, WHITE)
    # coordenadas de texto
    rank1_coord_rect = rank1_text.get_rect(center=(3 * WIDTH / 10, 0.4 * HEIGHT))
    rank2_coord_rect = rank2_text.get_rect(center=(3 * WIDTH / 10, 0.5 * HEIGHT))
    rank3_coord_rect = rank3_text.get_rect(center=(3 * WIDTH / 10, 0.6 * HEIGHT))
    rank4_coord_rect = rank4_text.get_rect(center=(3 * WIDTH / 10, 0.7 * HEIGHT))
    rank5_coord_rect = rank5_text.get_rect(center=(3 * WIDTH / 10, 0.8 * HEIGHT))
    # dibujo texto
    window.blit(rank1_text, rank1_coord_rect)
    window.blit(rank2_text, rank2_coord_rect)
    window.blit(rank3_text, rank3_coord_rect)
    window.blit(rank4_text, rank4_coord_rect)
    window.blit(rank5_text, rank5_coord_rect)

    # ---------------------------------------------------------------------------------- COLUMNA SCORES Y NAMES
    score_and_name = [(800, "DNS"), (650, "JSG"), (500, "UQP"), (450, "APQ"), (350, "HHH")]
    # scores
    score1_text = font.render(f"{score_and_name[0]}", True, WHITE)
    score2_text = font.render(f"{score_and_name[1]}", True, WHITE)
    score3_text = font.render(f"{score_and_name[2]}", True, WHITE)
    score4_text = font.render(f"{score_and_name[3]}", True, WHITE)
    score5_text = font.render(f"{score_and_name[4]}", True, WHITE)
    # names
    name1_text = font.render(f"{score_and_name[0]}", True, WHITE)
    name2_text = font.render(f"{score_and_name[1]}", True, WHITE)
    name3_text = font.render(f"{score_and_name[2]}", True, WHITE)
    name4_text = font.render(f"{score_and_name[3]}", True, WHITE)
    name5_text = font.render(f"{score_and_name[4]}", True, WHITE)
    # ----------------------------------------------------------------------------------- COLUMNA SCORES
    # asigno valores a top_scores TODO valores top_score tengo que asignarlos mediante Model_Leaderboards
    top_scores = (1000, 600, 450, 300, 150)
    # valores top
    top_score1 = top_scores[0]
    top_score2 = top_scores[1]
    top_score3 = top_scores[2]
    top_score4 = top_scores[3]
    top_score5 = top_scores[4]
    # top scores
    top_score1_text = font.render(f"{top_score1}", True, WHITE)
    top_score2_text = font.render(f"{top_score2}", True, WHITE)
    top_score3_text = font.render(f"{top_score3}", True, WHITE)
    top_score4_text = font.render(f"{top_score4}", True, WHITE)
    top_score5_text = font.render(f"{top_score5}", True, WHITE)
    # coordenadas de texto
    top_score1_coord_rect = top_score1_text.get_rect(center=(5 * WIDTH / 10, 0.4 * HEIGHT))
    top_score2_coord_rect = top_score2_text.get_rect(center=(5 * WIDTH / 10, 0.5 * HEIGHT))
    top_score3_coord_rect = top_score3_text.get_rect(center=(5 * WIDTH / 10, 0.6 * HEIGHT))
    top_score4_coord_rect = top_score4_text.get_rect(center=(5 * WIDTH / 10, 0.7 * HEIGHT))
    top_score5_coord_rect = top_score5_text.get_rect(center=(5 * WIDTH / 10, 0.8 * HEIGHT))
    # dibujo texto
    window.blit(top_score1_text, top_score1_coord_rect)
    window.blit(top_score2_text, top_score2_coord_rect)
    window.blit(top_score3_text, top_score3_coord_rect)
    window.blit(top_score4_text, top_score4_coord_rect)
    window.blit(top_score5_text, top_score5_coord_rect)

# ---------------------------------------------------------------------------------- COLUMNA NAMES
    # asigno nombres al vector names
    names = ("DNS", "STP", "SFD", "GHT", "RLP")
    # names
    name1_text = font.render(f"{names[0]}", True, WHITE)
    name2_text = font.render(f"{names[1]}", True, WHITE)
    name3_text = font.render(f"{names[2]}", True, WHITE)
    name4_text = font.render(f"{names[3]}", True, WHITE)
    name5_text = font.render(f"{names[4]}", True, WHITE)
    # coordenadas de texto
    name1_coord_rect = name1_text.get_rect(center=(7 * WIDTH / 10, 0.4 * HEIGHT))
    name2_coord_rect = name2_text.get_rect(center=(7 * WIDTH / 10, 0.5 * HEIGHT))
    name3_coord_rect = name3_text.get_rect(center=(7 * WIDTH / 10, 0.6 * HEIGHT))
    name4_coord_rect = name4_text.get_rect(center=(7 * WIDTH / 10, 0.7 * HEIGHT))
    name5_coord_rect = name5_text.get_rect(center=(7 * WIDTH / 10, 0.8 * HEIGHT))
    # dibujo texto
    window.blit(name1_text, name1_coord_rect)
    window.blit(name2_text, name2_coord_rect)
    window.blit(name3_text, name3_coord_rect)
    window.blit(name4_text, name4_coord_rect)
    window.blit(name5_text, name5_coord_rect)

# ---------------------------------------------------------------------------------- DIBUJO BOTÓN PARA ATRÁS
    # dibujo botón para volver al menú
    polygon_points = ([30, 60], [75, 30], [75, 90])
    pygame.draw.polygon(window, BLACK, polygon_points)
    pygame.draw.polygon(window, RED, polygon_points, 5)

    # actualizo ventana
    pygame.display.flip()

# ---------------------------------------------------------------------------------- BUCLE PRUEBA
    # bucle prueba
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if pygame.draw.polygon(window, BLACK, polygon_points).collidepoint(mouse_pos):
                        Menu()
                        run = False

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
    subtitle_volume = font2.render("10-100", True, BLUE)
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

    # dibujo botón para volver al menú
    polygon_points = ([30, 60], [75, 30], [75, 90])
    pygame.draw.polygon(window, RED, polygon_points)
    pygame.draw.polygon(window, RED, polygon_points, 5)
    pygame.display.update()
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

    running = True
    clock = pygame.time.Clock()
    while running:
        time_delta = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if pygame.draw.polygon(window, BLACK, polygon_points).collidepoint(mouse_pos):
                        Menu()
                        running = False
                        sys.exit()

            manager.process_events(event)
        manager.update(time_delta)

        manager.draw_ui(window)

        pygame.display.update()


Menu()
pygame.quit()