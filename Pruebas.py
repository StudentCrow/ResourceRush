import pygame, pygame.surfarray
from pygame.locals import *
from Viewer_Bit import ViewerBit; from ModelBit import ModelBit
from ViewLocation import ViewLocation
from ModelATXLocation import ModelATX; from ModelGPULocation import ModelGPU
from ViewOrder import ViewOrder; from ModelOrder import ModelOrder
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

    ATX = ViewLocation("ATX", 200, 540); GPU = ViewLocation("GPU", 1720, 540)
    view_locations = [ATX, GPU]
    model_ATX = ModelATX(ATX.name, ATX.x, ATX.y); model_GPU = ModelGPU(GPU.name, GPU.x, GPU.y)
    model_locations = [model_ATX, model_GPU]
    model_bit_prueba = ModelBit("1", view_locations, posx, posy)

    first_pos = (int, int)
    bit_prueba = ViewerBit(screen, posx, posy)
    bit_prueba.drawBit()

    OrderBox = ViewOrder(screen_res)
    OrderBox.drawOrder(screen)

    pygame.display.update()

    # counter = 30
    # timer = 1000
    # timer_event = pygame.USEREVENT + 1
    # pygame.time.set_timer(timer_event, timer)

    run = True
    selection_on = False
    order_on = False
    send_order = False
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
                # elif event.key == pygame.K_LEFT:
                #     if not left and not model_bit_prueba.GoToCheck:
                #         left = True
                #         model_bit_prueba.GoToCheck = True
                # elif event.key == pygame.K_RIGHT:
                #     if not right and not model_bit_prueba.GoToCheck:
                #         right = True
                #         model_bit_prueba.GoToCheck = True
                else:
                    if send_order:
                        ModelOrderBox.getOrder(event)
                        if ModelOrderBox.send:
                            send_order = False
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                if not selection_on and not order_on and not send_order:
                    if bit_prueba.bit_selected: bit_prueba.bit_selected = False
                    selection_on = True
                    first_pos = event.pos
                    selection = SelectionRectangle(event.pos)
                elif order_on and not selection_on and not send_order:
                    if not send_order:
                        send_order = True
                        ModelOrderBox = ModelOrder()
                        ModelOrder.exists = True
                elif not selection_on and not order_on and send_order:
                    send_order = False
                    ModelOrder.exists = False
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
                    for location in view_locations:
                        location.zoomLocation(event.y)
        if ModelOrder.exists:
            if ModelOrderBox.send and bit_prueba.bit_selected:
                model_bit_prueba.receive_order(ModelOrderBox.text)
                ModelOrder.exists = False
            elif ModelOrderBox.send and not bit_prueba.bit_selected:
                ModelOrderBox.text = ''
                ModelOrder.exists = False

        screen.fill((255, 255, 255))
        for location in view_locations:
            for model_location in model_locations:
                model_location.work()
                location.checkLocationCollision(pygame.mouse.get_pos())
                if location.name == model_location.name:
                    location.drawLocation(screen, model_location.functional)
                    if location.collided_check:
                        location.showFont(screen, model_location.power)
        if model_bit_prueba.GoToCheck:
            model_bit_prueba.go_to(model_bit_prueba.loc)
            bit_prueba.x = model_bit_prueba.x
            bit_prueba.y = model_bit_prueba.y
        bit_prueba.drawBit()
        if selection_on:
            selection.drawSelection(screen)
        if not selection_on:
            order_on = OrderBox.checkOrderCollision(pygame.mouse.get_pos())
        OrderBox.drawOrder(screen)
        if send_order:
            OrderBox.drawOrderText(ModelOrderBox.text, screen, ModelOrderBox)
        pygame.display.update()
    pygame.quit()

if __name__ == '__main__': main()