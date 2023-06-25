import pygame, pygame.surfarray
from pygame.locals import *
from Viewer_Bit import ViewerBit; from ModelBit import ModelBit
from ModelLocation import ModelLocation
from SelectionRectangle import SelectionRectangle



def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen_res = pygame.display.Info()
    posx = screen_res.current_w/2 - 50/2
    posy = 540
    screen = pygame.display.set_mode((screen_res.current_w, screen_res.current_h), pygame.FULLSCREEN)
    pygame.display.set_caption("Resource Rush")
    screen.fill((255, 255, 255))

    Location1 = ModelLocation("One", 50, 540); Location2 = ModelLocation("Two", 1870, 540)
    model_bit_prueba = ModelBit("1", [Location1, Location2], posx, posy)

    # surf = pygame.surfarray.pixels3d(screen)
    # surf[:] = (255, 255, 255)
    # surf[::4, ::4] = (0, 0, 255)

    first_pos = (int, int)
    bit_prueba = ViewerBit(screen, posx, posy)
    bit_prueba.drawBit()

    OrderBox = Rect(screen_res.current_w-450, screen_res.current_h-100, 450, 100)
    pygame.draw.rect(screen, (0, 0, 0), OrderBox)

    pygame.display.update()

    # counter = 30
    # timer = 1000
    # timer_event = pygame.USEREVENT + 1
    # pygame.time.set_timer(timer_event, timer)

    run = True
    selection_on = False
    left = False; right = False
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # elif event.type == timer_event:
            #     counter -= 1
            #     if counter == 0:
            #         run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                elif event.key == pygame.K_LEFT:
                    if not left and not model_bit_prueba.GoToCheck:
                        left = True
                        model_bit_prueba.GoToCheck = True
                elif event.key == pygame.K_RIGHT:
                    if not right and not model_bit_prueba.GoToCheck:
                        right = True
                        model_bit_prueba.GoToCheck = True
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                if not selection_on:
                    selection_on = True
                    first_pos = event.pos
                    selection = SelectionRectangle(event.pos)
            elif event.type == MOUSEMOTION:
                if selection_on:
                    selection.updateSelection(event.pos)
                    bit_prueba.checkBitSelection(first_pos, event.pos)
            elif event.type == MOUSEBUTTONUP and event.button == 1:
                if selection_on:
                    selection_on = False
            elif event.type == MOUSEWHEEL:
                if not selection_on:
                    bit_prueba.zoomBit(event.y)

        screen.fill((255, 255, 255))
        if model_bit_prueba.GoToCheck:
            if left:
                model_bit_prueba.go_to("One")
                bit_prueba.x = model_bit_prueba.x
                bit_prueba.y = model_bit_prueba.y
                if not model_bit_prueba.GoToCheck:
                    left = False
            elif right:
                model_bit_prueba.go_to("Two")
                bit_prueba.x = model_bit_prueba.x
                bit_prueba.y = model_bit_prueba.y
                if not model_bit_prueba.GoToCheck:
                    right = False
        bit_prueba.drawBit()
        if selection_on:
            selection.drawSelection(screen)
        pygame.draw.rect(screen, (0, 0, 0), OrderBox)
        pygame.display.update()
    pygame.quit()

if __name__ == '__main__': main()