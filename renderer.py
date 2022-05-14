import pygame
from pygame.locals import *
from item import Item
from river import River
from pile import Pile
from menu import Menu
from settings import Settings

class Renderer:

    def __init__(self):
        self.running = True
        self.surface = None
        self.size = self.width, self.height = 640, 400
        self.color = (255,255,255)

        

        # States: 
        # Menu state:     0
        # River State:    1
        # Pile State:     2
        # Settings State: 3
        self.state = 0

    def on_init(self):
        pygame.init()
        self.surface = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.running = True

        self.dot = Item(12, 15)
        #self.menu = Menu(self)
        self.pile = Pile()
        self.river = River()
        self.settings = Settings()

    #Event listener
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
            
        
        #if self.state == 0:
            #self.menu.update(event)
        #elif self.state == 1:
            #self.river.update(event)
        #elif self.state == 2:
            #self.pile.update(event)
        #else:
            #self.settings.update(event)

    # Render updater
    def on_render(self):
        new_surface = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.surface.blit(new_surface, (0, 0))


        #self.dot.draw(self.surface)
        #self.dot.update()

        self.pile.draw(self.surface)
        self.pile.update()
        

        # if self.state == 0:
        #     self.menu.render(self.surface)
        # elif self.state == 1:
        #     self.river.render()
        # elif self.state == 2:
        #     self.pile.render()
        # else:
        #    self.settings.render()

        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self.running = False

        # Main game loop
        while( self.running ):

            for event in pygame.event.get():
                self.on_event(event)

            
            self.on_render()
        
        # Exiting
        self.on_cleanup()
 
if __name__ == "__main__" :
    window = Renderer()
    window.on_execute()