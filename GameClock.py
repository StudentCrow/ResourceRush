import pygame

pygame.init()
window = pygame.display.set_mode((200, 200))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 100)
counter = 30
timer = 1000
time_warp = 0
time_running = True
text = font.render(str(counter), True, (0, 128, 0))

timer_event = pygame.USEREVENT+1
pygame.time.set_timer(timer_event, timer)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == timer_event:
            counter -= 1
            text = font.render(str(counter), True, (0, 128, 0))
            if counter == 0:
                run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and time_warp > -2 and time_running:
                timer -= 250
                pygame.time.set_timer(timer_event, timer)
                time_warp -= 1
            elif event.key == pygame.K_RIGHT and time_warp < 2 and time_running:
                timer += 250
                pygame.time.set_timer(timer_event, timer)
                time_warp += 1
            elif event.key == pygame.K_SPACE:
                if time_running:
                    pygame.time.set_timer(timer_event, 0)
                    time_running = False
                else:
                    pygame.time.set_timer(timer_event, timer)
                    time_running = True


    window.fill((255, 255, 255))
    text_rect = text.get_rect(center = window.get_rect().center)
    window.blit(text, text_rect)
    pygame.display.flip()