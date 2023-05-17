from Resources import *
from Viewer_Menu import *
from Model_Leaderboards import *
import pygame
pygame.init()

def leaderboards():
    # creación ventana, título y background
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Resource Rush")
    img_background = pygame.image.load("img/Leaderboards.png")        # TODO dibujar el background del leaderboards
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

# ---------------------------------------------------------------------------------- COLUMNA SCORES
    # asigno valores a top_scores TODO valores top_score tengo que asignarlos mediante Model_Leaderboards
    top_scores = (200, 400, 100, 600, 550)
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
    # valores name
    name1 = names[0]
    name2 = names[1]
    name3 = names[2]
    name4 = names[3]
    name5 = names[4]
    # names
    name1_text = font.render(f"{name1}", True, WHITE)
    name2_text = font.render(f"{name2}", True, WHITE)
    name3_text = font.render(f"{name3}", True, WHITE)
    name4_text = font.render(f"{name4}", True, WHITE)
    name5_text = font.render(f"{name5}", True, WHITE)
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
    pygame.draw.polygon(window, BLACK, ([30, 60], [75, 30], [75, 90]))
    pygame.draw.polygon(window, RED, ([30, 60], [75, 30], [75, 90]), 5)

    # actualizo ventana
    pygame.display.flip()

# ---------------------------------------------------------------------------------- BUCLE PRUEBA
    # bucle prueba
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


if __name__ == "__main__":
    leaderboards()

pygame.quit()