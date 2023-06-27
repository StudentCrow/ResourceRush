import pygame, pygame.surfarray
from pygame.locals import *

class SelectionRectangle:
    def __init__(self, first_pos):
        self.first_pos = first_pos
        self.mouse_pos = first_pos
        # self.left = int
        # self.top = int
        # self.width = int
        # self.height = int
        self.color = (0, 0, 0)

    #Function to update the new selection area
    def updateSelection(self, mouse_pos):
        self.mouse_pos = mouse_pos

    #Function to draw the selection rectangle
    def drawSelection(self, screen):
        rect = Rect(min(self.first_pos[0], self.mouse_pos[0]), min(self.first_pos[1], self.mouse_pos[1]),
                    abs(self.first_pos[0]-self.mouse_pos[0]), abs(self.first_pos[1]-self.mouse_pos[1]))
        pygame.draw.rect(screen, self.color, rect, 1)


# def main():
#     """ main()
#     Simple test program for showing off the selection rectangles
#     """
#     pygame.init()
#     screen = pygame.display.set_mode((640, 480), 0, 24)
#
#     # create a dotted background
#     surf = pygame.surfarray.pixels3d(screen)
#     surf[:] = (255, 255, 255)
#     surf[::4, ::4] = (0, 0, 255)
#     pygame.display.update()
#
#     # make up a test loop
#     finished = 0
#     selection_on = 0
#     while not finished:
#         for e in pygame.event.get():
#             if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
#                 finished = 1
#             elif e.type == MOUSEBUTTONDOWN and e.button == 1:
#                 if not selection_on:
#                     # begin with selection as the user pressed down the left
#                     # mouse button
#                     selection_on = 1
#                     selection = SelectionRect(screen, e.pos)
#             elif e.type == MOUSEMOTION:
#                 if selection_on:
#                     # update the selection rectangle while the mouse is moving
#                     selection.updateRect(e.pos)
#                     selection.draw(screen)
#             elif e.type == MOUSEBUTTONUP and e.button == 1:
#                 if selection_on:
#                     # stop selection when the user released the button
#                     selection_on = 0
#                     rect = selection.updateRect(e.pos)
#                     # don't forget this!
#                     # (or comment it out if you really want the final selection
#                     #  rectangle to remain visible)
#                     selection.hide(screen)
#                     # just FYI
#                     print ("Final selection rectangle:", rect)
#
#     pygame.quit()
#
#
#if __name__ == '__main__': main()