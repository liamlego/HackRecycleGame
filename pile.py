import pygame
import os
from pygame.locals import *
from bin import Bins
from item import Item
import random

class Pile(pygame.sprite.Sprite):

    # takes width and height of window as params
    def __init__(self, width, height):
        super().__init__()
        self.count = 0
        self.finished = False
        # initialize image and rect

        self.image = pygame.image.load(os.path.join("images","pile.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = width / 2, height / 2 - (height / 4)

        self.bins = Bins()

        self.item = Item(0, 2, 2)

    def spawnItem(self, event):
        type = random.randint(0,11)
        self.item = Item(type, 2, 2)


    def render(self, screen):
        screen.blit(self.image, self.rect)
        self.bins.render(screen)
        self.item.draw(screen)
        
    # decreases size of pile
    def update(self, gamelogic, event):

        self.item.update(event)

        if event.type == MOUSEBUTTONDOWN and self.finished == False:

            # Check pile click
            self.count += 1
            if(self.count % 3 == 0):
                if self.rect.collidepoint(event.pos):
                    # adjust size of image
                    size = self.image.get_width() * .9, self.image.get_height() * .9
                    self.image = pygame.transform.scale(self.image, size)
                    
                    # adjust size and position of rect
                    self.rect.inflate_ip(self.image.get_width() * .9, self.image.get_height() * .9)
                    self.rect.move_ip(self.image.get_width() / 2, self.image.get_height() / 2)
                    
                    # pick up item
                    self.spawnItem(event)

            if(self.count == 15):
                self.finished = True
                self.rect.move_ip(1000, 1000)
    
