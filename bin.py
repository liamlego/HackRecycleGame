import pygame
import os
from pygame.locals import *

class Bin(pygame.sprite.Sprite):
    def __init__(self, path, x, y, width, height, type):
        super().__init__()

        self.image = pygame.image.load(os.path.join("images/bins", path))
        self.rect = self.image.get_rect()

        self.type = type
        self.rect.width = width
        self.rect.height = height

        self.rect.center = (x,y)
        self.collision_rect = pygame.Rect(0, 0, width/3, height/2)
        self.collision_rect.center = self.rect.x + width / 2, self.rect.y + height / 2
        
        self.moving = False

    def render(self, screen):
        screen.blit(self.image, self.rect)

    def eat(self):
        pygame.mixer.music.load("sounds/putInTrash.wav")
        pygame.mixer.music.play()

class Bins:
    def __init__(self):
        self.plasticbin = Bin("plasticbin.png", 205, 505, 180, 256, 3)
        self.metalbin = Bin("metalbin.png", 455, 505, 180, 256, 1)
        self.glassbin = Bin("glassbin.png", 705, 505, 182, 255, 0)
        self.paperbin = Bin("paperbin.png", 955, 505, 179, 255, 2)
        self.trashbin = Bin("trashbin.png", 1205, 505, 180, 253, 4)
        
        self.bins = (self.plasticbin, self.paperbin, self.metalbin, self.glassbin, self.trashbin)

    def render(self, screen):
        for bin in self.bins:
            bin.render(screen)

    def getBins(self):
        return self.bins
