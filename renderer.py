import pygame
import os
from pygame.locals import *
from item import Item
from river import RiverScene
from pile import Pile
from menu import Menu
from bin import Bins
from gameLogic import GameLogic


class Renderer:

    def __init__(self):
        self.running = True
        self.surface = None
        self.size = self.width, self.height = 1400, 900
        
        self.color = (255,255,255)

    def on_init(self):
        pygame.init()
        self.surface = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.running = True

        self.menu = Menu(self)
        self.pile = Pile(self.width, self.height)
        self.river = RiverScene(self.width, self.height)
        self.bins = Bins()

        self.logic = GameLogic()
        self.item = Item(0, (2,2))

    #Event listener
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
        if self.logic.getState() == 0:
            self.menu.update(self.logic, event)
        elif self.logic.getState() == 2:
            self.river.update(self.logic, event)
        elif self.logic.getState() == 1:
            self.pile.update(self.logic, event)

    # Render updater
    def on_render(self):
        new_surface = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.surface.blit(new_surface, (0, 0))
        
        if self.logic.getState() == 0:
            self.menu.render(self.surface)
        elif self.logic.getState() == 2:
            self.river.render(self.surface, self.logic)
        elif self.logic.getState() == 1:
            self.pile.render(self.surface, self.logic)

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