import pygame.draw

class ViewerBit:
    def __init__(self, display, name, x = 0, y = 0, fill_color = (255, 255, 255), size = 50):
        self.name = name
        self.display = display
        self.x = x
        self.y = y
        self.size = size
        self.fill_color = fill_color
        self.border_color = (0, 0, 0)
        self.fixing_color = (0, 0, 255)
        self.bit_selected = False

    #Function to draw the full bit
    def drawBit(self, fixing):
        pygame.draw.rect(self.display, self.fill_color, (self.x-self.size/2, self.y-self.size/2, self.size, self.size), 0)
        if fixing:
            pygame.draw.rect(self.display, self.fixing_color, (self.x-self.size/2, self.y-self.size/2, self.size, self.size), 5)
        else:
            pygame.draw.rect(self.display, self.border_color, (self.x-self.size/2, self.y-self.size/2, self.size, self.size), 5)
        if self.bit_selected:
            pygame.draw.rect(self.display, (255, 255, 0), (self.x-self.size/2, self.y-self.size/2, self.size, self.size), 2)

    #Function to check if a bit is being selected
    def checkBitSelection(self, first_pos, last_pos):
        x_list = [first_pos[0], last_pos[0]]
        x_list.sort()
        y_list = [first_pos[1], last_pos[1]]
        y_list.sort()
        if self.x <= x_list[1] and self.x >= x_list[0]:
            if self.y <= y_list[1] and self.y >= y_list[0]:
                self.bit_selected = True
            else:
                self.bit_selected = False
        else:
            self.bit_selected = False

    #Function to resize the bit
    def zoomBit(self, direction):
        min_size = 50-40
        max_size = 50+40
        if direction == 1 and self.size < max_size:
            self.size += 10
        elif direction == -1 and self.size > min_size:
            self.size -= 10

    def showFont(self, text):
        info_font = pygame.font.SysFont('arial', round(self.size*2*0.25))
        text_image = info_font.render(str(text), True, self.border_color)
        text_rect = text_image.get_rect(center=(self.x, self.y - self.size/2 - 15))
        self.display.blit(text_image, text_rect)

    def checkBitCollision(self, mouse_pos):
        rect = pygame.Rect(self.x-self.size/2, self.y-self.size/2, self.size, self.size)
        return pygame.Rect.collidepoint(rect, mouse_pos)