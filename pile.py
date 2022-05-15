import pygame
import os
from pygame.locals import *
from bin import Bins
from item import Item
import random

from status import Status

class Pile(pygame.sprite.Sprite):

    # takes width and height of window as params
    def __init__(self, width, height):
        super().__init__()
        self.count = 0
        self.finished = False
        self.itempicked = False
        self.draw_item = False
        self.w, self.h = width, height

        # end text
        self.font = pygame.font.Font('freesansbold.ttf', 45)
        self.text = self.font.render("Congratulations you finished!", True, (255,255,255))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.w / 2, self.h / 2)

        # initialize image and rect
        self.image = pygame.image.load(os.path.join("images","pile.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = self.w / 2, self.h / 2 - (self.h / 4)

        self.bins = Bins()

        self.item = Item(0, (0,0))

        self.status = Status(width, height)


    def spawnItem(self):
        type = random.randint(0,11)
        self.item = Item(type, pygame.mouse.get_pos())
        self.item.moving = True
        self.itempicked = True
        self.draw_item = True
        

    def reset(self, gamelogic):
        self.finished = False
        self.image = pygame.image.load(os.path.join("images","pile.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = self.w / 2, self.h / 2 - (self.h / 4)
        gamelogic.setScore(0)
        self.draw_item = False
        self.itempicked = False
        self.count = 0
        

    def render(self, screen):
        if not self.finished:
            screen.blit(self.image, self.rect)
            pygame.draw.rect(screen, (255,255,255), self.rect, 1)
            self.bins.render(screen)
            if self.draw_item:
                self.item.draw(screen)
        else:
            screen.blit(self.text, self.text_rect)
        self.status.render(screen)
        
    # decreases size of pile
    def update(self, gamelogic, event):

        #self.item.update(event, self.bins, gamelogic)
        self.status.update(gamelogic, event, gamelogic.getScore(), self)

        if event.type == MOUSEBUTTONDOWN and self.finished == False:

            # Check pile click
            if not self.itempicked:
                if self.rect.collidepoint(event.pos):
                    self.count += 1
                    if(self.count % 3 == 0):
                        # adjust size of image
                        size = self.image.get_width() * .9, self.image.get_height() * .9
                        self.image = pygame.transform.scale(self.image, size)
                        
                        # adjust size and position of rect
                        self.rect.width, self.rect.height = self.image.get_width(), self.image.get_height()
                        self.rect.move_ip(15, 22)
                        
                    # pick up item
                    self.spawnItem()
                    self.draw_item = True
                    
            # elif "Please sort the item you have picked before trying to spick another"

        if self.item.update(event, self.bins, gamelogic):
            if self.count == 15:
                self.finished = True
            self.draw_item = False
            self.itempicked = False
