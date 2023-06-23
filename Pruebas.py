import pygame, pygame.surfarray
from pygame.locals import *
from Viewer_Bit import ViewerBit
from SelectionRectangle import SelectionRect



def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen_res = pygame.display.Info()
    screen = pygame.display.set_mode((screen_res.current_w, screen_res.current_h), pygame.FULLSCREEN)
    pygame.display.set_caption("Resource Rush")
    screen.fill((255, 255, 255))

    # surf = pygame.surfarray.pixels3d(screen)
    # surf[:] = (255, 255, 255)
    # surf[::4, ::4] = (0, 0, 255)

    first_pos = (int, int)
    bit_prueba = ViewerBit(screen, screen_res.current_w/2 - 50/2, screen_res.current_h/2 - 50/2)
    bit_prueba.drawBit()

    pygame.display.update()

    counter = 30
    timer = 1000
    timer_event = pygame.USEREVENT + 1
    pygame.time.set_timer(timer_event, timer)

    run = True
    selection_on = False
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                run = False
            elif event.type == timer_event:
                counter -= 1
                if counter == 0:
                    run = False
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                if not selection_on:
                    selection_on = True
                    selection = SelectionRect(screen, event.pos)
                    first_pos = event.pos
            elif event.type == MOUSEMOTION:
                if selection_on:
                    selection.updateRect(event.pos)
                    selection.draw(screen)
                    bit_prueba.checkBitSelection(first_pos, event.pos)
            elif event.type == MOUSEBUTTONUP and event.button == 1:
                if selection_on:
                    selection_on = False
                    rect = selection.updateRect(event.pos)
                    selection.hide(screen)
                    print("Final selection rectangle:", rect)
            elif event.type == MOUSEWHEEL:
                if not selection_on:
                    bit_prueba.zoomBit(event.y)
        if not selection_on:
            screen.fill((255, 255, 255))
        bit_prueba.drawBit()
        pygame.display.update()
    pygame.quit()

if __name__ == '__main__': main()