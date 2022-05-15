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
        self.start = True

        # finished pop out window
        self.font = pygame.font.Font('freesansbold.ttf', 45)
        self.text = self.font.render("Congratulations you finished!", True, (255,255,255))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.w / 2, self.h / 2)

        self.endpopout_rect = pygame.Rect((self.w / 2) - 300, (self.h / 2) - 230, 500, 500)
        self.endsurface1 = pygame.image.load(os.path.join("images/start_end", "greatFinish.png")).convert_alpha()
        self.endsurface2 = pygame.image.load(os.path.join("images/start_end", "goodFinish.png")).convert_alpha()
        self.endsurface3 = pygame.image.load(os.path.join("images/start_end", "badFinish.png")).convert_alpha()

        self.startpopout_rect = pygame.Rect((self.w / 2) - 300, (self.h / 2) - 230, 500, 500)
        self.startsurface = pygame.image.load(os.path.join("images/start_end", "pileInstructions.png")).convert_alpha()

        self.startbutton = pygame.Rect(self.startpopout_rect.x + 80, self.startpopout_rect.y + 388, 440, 50)
        self.endbutton = pygame.Rect(self.endpopout_rect.x + 80, self.endpopout_rect.y + 388, 440, 50)


        # initialize image and rect
        self.image = pygame.image.load(os.path.join("images","pile.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = self.w / 2, self.h / 2 - (self.h / 4)

        self.bins = Bins()

        self.item = Item(0, (0,0))

        self.status = Status(width, height)

    # spawn random recycle/ trash item
    def spawnItem(self):
        type = random.randint(0, 14)
        self.item = Item(type, pygame.mouse.get_pos())
        self.item.moving = True
        self.itempicked = True
        self.draw_item = True
        

    def reset(self, gamelogic):
        self.finished = False
        self.draw_item = False
        self.itempicked = False
        self.count = 0
        self.start = True
        self.status.colorScore((255,255,255), gamelogic)
        self.status.moveScore(self.w - 100, 50)
        

    def render(self, screen, gamelogic):
        if self.start:
            screen.blit(self.startsurface, self.startpopout_rect)
            self.image = pygame.image.load(os.path.join("images","pile.png")).convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.center = self.w / 2, self.h / 2 - (self.h / 4)
            gamelogic.setScore(0)
            gamelogic.setState(1)
        else:
            if not self.finished:
                screen.blit(self.image, self.rect)

            self.bins.render(screen)
            if self.draw_item:
                self.item.draw(screen)

            if self.finished:
                if gamelogic.getScore() > 250:
                    screen.blit(self.endsurface1, self.endpopout_rect)
                elif gamelogic.getScore() > 50:
                    screen.blit(self.endsurface2, self.endpopout_rect)
                else: 
                    screen.blit(self.endsurface3, self.endpopout_rect)
                self.status.moveScore(560, 322)
                self.status.colorScore((65, 170, 47), gamelogic)
                
        self.status.render(screen)

        
        
    # decreases size of pile
    def update(self, gamelogic, event):
        if event.type == MOUSEBUTTONDOWN and self.start and self.startbutton.collidepoint(event.pos):
            self.start = False

        if event.type == MOUSEBUTTONDOWN and self.finished and self.endbutton.collidepoint(event.pos):
            self.reset(gamelogic)

        #self.item.update(event, self.bins, gamelogic)
        self.status.update(gamelogic, event, gamelogic.getScore(), self)

        if event.type == MOUSEBUTTONDOWN and not self.finished and not self.start:

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
                    
        if self.item.update(event, self.bins, gamelogic):
            if self.count == 15:
                self.finished = True
            self.draw_item = False
            self.itempicked = False