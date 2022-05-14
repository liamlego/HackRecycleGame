import pygame
from pygame.locals import *
 
class Renderer:

    def __init__(self):
        self.running = True
        self.surface = None
        self.size = self.weight, self.height = 640, 400
        self.color = (255,255,255)
 
    def on_init(self):
        pygame.init()
        self.surface = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.running = True
 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
            
    def on_render(self):
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self.running = False
 
        while( self.running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__" :
    window = Renderer()
    window.on_execute()