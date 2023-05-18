# TODO falta hacer que interaccionen con la selección del ratón
import pygame

from Imports import *
pygame.init()

# Dimensiones bit
x_bit_min = 5
y_bit_min = 5
x_bit_max = 10
y_bit_max = 10

# Creo ventana y título de ventana
window = pygame.display.set_mode(WINDOW_DIM)
pygame.display.set_caption("Resource Rush")

# Coordenadas y dimensiones del bit
bit_rect = pygame.draw.rect(window, WHITE, (0.5 * WIDTH, 0.5 * WIDTH, x_bit_max, y_bit_max))


arrastrando = False
inicio_seleccion = None
final_seleccion = None

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                arrastrando = True
                inicio_seleccion = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if arrastrando:
                    arrastrando = False
                final_seleccion = pygame.mouse.get_pos()
                print("Posición inicial:", inicio_seleccion)
                print("Posición final:", final_seleccion)


    pygame.display.flip()

pygame.quit()