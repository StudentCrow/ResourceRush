import pygame, pygame.surfarray
from pygame.locals import *
from Viewer_Bit import ViewerBit



def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((640, 480), 0, 24)
    pygame.display.set_caption("Resource Rush")
    screen.fill((255, 255, 255))

    # surf = pygame.surfarray.pixels3d(screen)
    # surf[:] = (255, 255, 255)
    # surf[::4, ::4] = (0, 0, 255)

    bit_prueba = ViewerBit(screen, 320, 240)
    bit_prueba.draw_bit()

    pygame.display.update()

    counter = 30
    timer = 1000
    timer_event = pygame.USEREVENT + 1
    pygame.time.set_timer(timer_event, timer)

    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == timer_event:
                counter -= 1
                if counter == 0:
                    run = False
    pygame.quit()

if __name__ == '__main__': main()