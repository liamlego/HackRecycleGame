import pygame
import os
from pygame.locals import *
from bin import Bins
from item import Item
import random

from status import Status

class RiverScene:

    # takes width and height of window as params
    def __init__(self, width, height):
        self.count = 0
        self.finished = False
        self.itempicked = False
        self.draw_item = False
        self.width, self.height = width, height

        self.bins = Bins()
        self.item = Item(0, (0,0))
        self.status = Status(width, height)

        self.count = 0

        self.items = []

    def spawnItem(self, location):
        type = random.randint(0,11)

        item = Item(type, location)
        item.setSpeed(3)

        self.items.append(item)
        

    def reset(self, gamelogic):
        self.finished = False
        """
        self.finished = False
        self.rect = self.image.get_rect()
        self.rect.center = self.w / 2, self.h / 2 - (self.h / 4)
        gamelogic.setScore(0)
        self.draw_item = False
        self.itempicked = False
        self.count = 0
        """
        gamelogic.setScore(0)
        


    def render(self, screen):
        if not self.finished:
            self.bins.render(screen)
            if self.draw_item:
                self.item.draw(screen)
        else:
            screen.blit(self.text, self.text_rect)
        self.status.render(screen)

        for item in self.items:
            item.draw(screen)
        
    # decreases size of pile
    def update(self, gamelogic, event):
        self.status.update(gamelogic, event, gamelogic.getScore(), self)

        if self.count%100 == 0:
            # Spawn item at beginning of river

            self.spawnItem((500, 250))
            
            self.count = 0
        
        self.count = self.count + 1
        for item in self.items:
            if item.rect.x+item.rect.width/2 >= self.width:
                self.items.remove(item)
                gamelogic.setScore(gamelogic.getScore()-5)

            if item.update(event, self.bins, gamelogic):
                self.draw_item = False
                self.itempicked = False
                self.items.remove(item)
            else:
                item.moveWithSpeed()
