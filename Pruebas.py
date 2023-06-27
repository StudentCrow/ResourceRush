import pygame, pygame.surfarray
from pygame.locals import *
from Viewer_Bit import ViewerBit; from ModelBit import ModelBit
from ViewLocation import ViewLocation
from ModelATXLocation import ModelATX; from ModelGPULocation import ModelGPU; from ModelCPULocation import ModelCPU
from ModelPeriLocation import ModelPERI; from ModelRAMLocation import ModelRAM; from ModelVentLocation import ModelVENT
from ModelVRMLocation import ModelVRM; from ModelChipsetLocation import ModelCHIPSET
from ViewOrder import ViewOrder; from ModelOrder import ModelOrder
from SelectionRectangle import SelectionRectangle


def loadLocations(screenx, screeny):
    loc_name = ['ATX', 'CHIPSET', 'CPU', 'GPU',
                'PERI', 'RAM', 'VENT', 'VRM']
    positions = ['midleft', 'bottomleft', 'midbottom',
                 'bottomright', 'midright', 'topright'
                 , 'midtop', 'topleft']
    rect = Rect(200, 200, screenx-400, screeny-400)
    view_locations = []; model_locations = []
    for pos in positions:
        loc_pos = eval('rect.'+pos)
        name = loc_name[positions.index(pos)]
        code = name + '=ViewLocation("' + name + '",' + str(loc_pos[0]) + ',' + str(loc_pos[1]) + ')'
        exec(code)
        code = 'view_locations.append('+name+')'
        exec(code)
        code = 'model_'+name+'=Model'+name+'("' + name + '",' + str(loc_pos[0]) + ',' + str(loc_pos[1]) + ')'
        exec(code)
        code = 'model_locations.append(model_'+name+')'
        exec(code)
    return view_locations, model_locations

def loadBits(quantity, center, screen, view_locations):
    odd = quantity%2
    number = int
    viewer_bits = []
    model_bits = []
    if odd == 0:
        number = int(quantity/2)
        name = 1
        for i in range(1, number+1):
            var = i*60
            code = 'bit_'+str(name)+'=ViewerBit(screen,"'+str(name)+'",center[0]-var,center[1])'
            exec(code)
            code = 'viewer_bits.append(bit_'+str(name)+')'
            exec(code)
            code = 'model_bit_'+str(name)+'=ModelBit("'+str(name)+'",view_locations,center[0]-var,center[1],var)'
            exec(code)
            code = 'model_bits.append(model_bit_'+str(name)+')'
            exec(code)
            name += 1
            code = 'bit_' + str(name) + '=ViewerBit(screen,"' + str(name) + '",center[0]+var,center[1])'
            exec(code)
            code = 'viewer_bits.append(bit_' + str(name) + ')'
            exec(code)
            code = 'model_bit_' + str(name) + '=ModelBit("' + str(name) + '",view_locations,center[0]+var,center[1],var)'
            exec(code)
            code = 'model_bits.append(model_bit_' + str(name) + ')'
            exec(code)
            name += 1
    else:
        number = int((quantity/2)-0.5)
        name = 1
        for i in range(0, number+1):
            var = i*60
            if i == 0:
                code = 'bit_' + str(name) + '=ViewerBit(screen,"' + str(name) + '",center[0],center[1])'
                exec(code)
                code = 'viewer_bits.append(bit_' + str(name) + ')'
                exec(code)
                code = 'model_bit_' + str(name) + '=ModelBit("' + str(name) + '",view_locations,center[0],center[1],var)'
                exec(code)
                code = 'model_bits.append(model_bit_' + str(name) + ')'
                exec(code)
                name += 1
            else:
                code = 'bit_' + str(name) + '=ViewerBit(screen,"' + str(name) + '",center[0]-var,center[1])'
                exec(code)
                code = 'viewer_bits.append(bit_' + str(name) + ')'
                exec(code)
                code = 'model_bit_' + str(name) + '=ModelBit("' + str(name) + '",view_locations,center[0]-var,center[1],var)'
                exec(code)
                code = 'model_bits.append(model_bit_' + str(name) + ')'
                exec(code)
                name += 1
                code = 'bit_' + str(name) + '=ViewerBit(screen,"' + str(name) + '",center[0]+var,center[1])'
                exec(code)
                code = 'viewer_bits.append(bit_' + str(name) + ')'
                exec(code)
                code = 'model_bit_' + str(name) + '=ModelBit("' + str(name) + '",view_locations,center[0]+var,center[1],var)'
                exec(code)
                code = 'model_bits.append(model_bit_' + str(name) + ')'
                exec(code)
                name += 1
    return viewer_bits, model_bits


def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen_res = pygame.display.Info()
    screen = pygame.display.set_mode((screen_res.current_w, screen_res.current_h), pygame.FULLSCREEN)
    pygame.display.set_caption("Resource Rush")
    screen.fill((255, 255, 255))

    view_locations, model_locations = loadLocations(screen_res.current_w, screen_res.current_h)
    pos_bit = screen.get_rect().center
    first_pos = (int, int)
    viewer_bits, model_bits = loadBits(3, pos_bit, screen, view_locations)

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
                    for bit in viewer_bits:
                        if bit.bit_selected: bit.bit_selected = False
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
                    for bit in viewer_bits:
                        bit.checkBitSelection(first_pos, event.pos)
            elif event.type == MOUSEBUTTONUP and event.button == 1:
                if selection_on:
                    selection_on = False
            elif event.type == MOUSEWHEEL:
                if not selection_on:
                    for bit in viewer_bits:
                        bit.zoomBit(event.y)
                    for location in view_locations:
                        location.zoomLocation(event.y)
        if ModelOrder.exists:
            if ModelOrderBox.send:
                for bit in viewer_bits:
                    if bit.bit_selected:
                        for model_bit in model_bits:
                            if model_bit.name == bit.name: model_bit.receive_order(ModelOrderBox.text);
                ModelOrder.exists = False

        screen.fill((255, 255, 255))
        for location in view_locations:
            for model_location in model_locations:
                model_location.work()
                collision = location.checkLocationCollision(pygame.mouse.get_pos())
                if location.name == model_location.name:
                    location.drawLocation(screen, model_location.functional)
                    if collision:
                        location.showFont(screen, model_location.power)
        for model_bit in model_bits:
            if model_bit.GoToCheck:
                model_bit.go_to(model_bit.loc)
                for bit in viewer_bits:
                    if bit.name == model_bit.name: bit.x = model_bit.x; bit.y = model_bit.y
        for bit in viewer_bits:
            bit_collision = bit.checkBitCollision(pygame.mouse.get_pos())
            if bit_collision:
                for model_bit in model_bits:
                    if model_bit.name == bit.name: bit.showFont(model_bit.load)

            bit.drawBit()
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