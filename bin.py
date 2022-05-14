import pygame
import os
from pygame.locals import *

class Bin(pygame.sprite.Sprite):
    def __init__(self, path, x, y, width, height):
        super().__init__()

        self.image = pygame.image.load(os.path.join("images/bins", path))
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.rect.width = width
        self.rect.height = height
        self.moving = False

    def render(self, screen):
        screen.blit(self.image, self.rect)

class Bins:
    def __init__(self):
        self.plasticbin = Bin("plasticbin.png", 50, 350, 10, 10)
        self.metalbin = Bin("metalbin.png", 300, 350, 10, 10)
        self.glassbin = Bin("glassbin.png", 550, 350, 10, 10)
        self.paperbin = Bin("paperbin.png", 800, 350, 10, 10)
        self.trashbin = Bin("trashbin.png", 1050, 350, 10, 10)
        
        self.bins = (self.plasticbin, self.paperbin, self.metalbin, self.glassbin, self.trashbin)

    def render(self, screen):
        for bin in self.bins:
            bin.render(screen)

    def getBins(self):
        return self.bins
