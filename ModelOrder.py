import pygame

class ModelOrder:
    """
    Model part class that gets the text orders
    to control the bits in the game
    """
    def __init__(self, text=''):
        self.text = text
        self.send = False

    #Function to write the orders
    def getOrder(self, event):  #Shall transform all inserted characters to capital letters
        if event.key == pygame.K_RETURN:    #Si se pulsa el intro
            self.send = True
        elif event.key == pygame.K_BACKSPACE:   #Si se pulsa el backspace
            self.text = self.text[:-1]  #Borra la última tecla del texto
        else:   #En caso de que se pulse cualquier otra tecla
            self.text += event.unicode.upper()  #Añade la tecla al texto

    #Function to get an order
    # def checkOrder(self):
    #     #Se resetean los valores y se devuelve la orden
    #     self.send = False
    #     Order = self.text
    #     self.text = ''
    #     return  Order