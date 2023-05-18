# modelo para insertar el nombre una vez se clique en new mission TODO falta acabar
import pygame
import pygame_gui
from Viewer_Menu import *

pygame.init()

# ventana
screen = pygame.display.set_mode(WIDTH, HEIGHT)
pygame.display.set_caption("RESOURCE RUSH")
# administrador de interfaz
manager = pygame_gui.UIManager(WIDTH, HEIGHT)
# cuadro de texto
text_entry = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((50, 100), (300, 50)), manager=manager)
text_entry.set_allowed_characters("abcdefghijklmnopqrstuvwxyz")
text_entry.set_text_length_limit(3)

# bucle prueba
running = True
clock = pygame.time.Clock()

while running:
    time_delta = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        manager.process_events(event)
    manager.update(time_delta)

    screen.fill(BLACK)

    manager.draw_ui(screen)

    pygame.display.update()

pygame.quit()
