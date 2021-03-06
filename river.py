import pygame
import os
from pygame.locals import *
from bin import Bins
from item import Item
import random

from status import Status

class RiverScene:

    # takes width and height of window as params
    def __init__(self, width, height, screen):
        self.count = 0
        self.start = True
        self.finished = False       # True if level is over
        self.itempicked = False     # True if item has been picked up
        self.draw_item = False      # True if item needs to be drawn
        self.width, self.height = width, height

        self.bins = Bins()
        self.item = Item(0, (0,0))
        self.status = Status(width, height)

        self.items = []

        self.item = None

        self.endpopout_rect = pygame.Rect((self.width / 2) - 300, (self.height / 2) - 230, 500, 500)
        self.endsurface1 = pygame.image.load(os.path.join("images/start_end", "greatFinish.png")).convert_alpha()
        self.endsurface2 = pygame.image.load(os.path.join("images/start_end", "goodFinish.png")).convert_alpha()
        self.endsurface3 = pygame.image.load(os.path.join("images/start_end", "badFinish.png")).convert_alpha()

        self.startpopout_rect = pygame.Rect((self.width / 2) - 300, (self.height / 2) - 230, 500, 500)
        self.startsurface = pygame.image.load(os.path.join("images/start_end", "riverInstructions.png")).convert_alpha()

        self.startbutton = pygame.Rect(self.startpopout_rect.x + 80, self.startpopout_rect.y + 388, 440, 50)
        self.endbutton = pygame.Rect(self.endpopout_rect.x + 80, self.endpopout_rect.y + 388, 440, 50)

        self.bg = pygame.image.load(os.path.join("images", "riverBackground.png"))
        self.bgrect = self.bg.get_rect()
        self.bgrect.x = 0
        self.bgrect.y = 0

        self.bgrect.width = 1400
        self.bgrect.height = 900
        screen.blit(self.bg, self.bgrect)

        self.speedcount = 1
        self.speed = 3

    # spawns a random item at given location
    def spawnItem(self, location):
        type = random.randint(0,14)

        item = Item(type, location)
        item.setSpeed(self.speed)

        self.items.append(item)
        
    # resets game score and images
    def reset(self, gamelogic):
        self.finished = False
        self.items.clear()
        gamelogic.setScore(0)
        self.count = 0
        self.start = True
        self.status.colorScore((0,0,0), gamelogic)
        self.status.moveScore(self.width - 100, 50)
        gamelogic.health = 3
        self.speed = 3
        self.itempicked = False
        self.item = None

    # render items in river scene
    def render(self, screen, gamelogic):
        if self.start:
            screen.blit(self.startsurface, self.startpopout_rect)
            gamelogic.setState(2)

        elif not self.finished:
            self.bins.render(screen)
            if self.draw_item:
                self.item.draw(screen)

            for item in self.items:
                item.draw(screen)
                item.moveWithSpeed()

        elif self.finished:
            # display correct endscreen
            if gamelogic.getScore() > 300:
                screen.blit(self.endsurface1, self.endpopout_rect)
            elif gamelogic.getScore() > 50:
                screen.blit(self.endsurface2, self.endpopout_rect)
            else: 
                screen.blit(self.endsurface3, self.endpopout_rect)
            self.status.moveScore(560, 322)
            self.status.colorScore((65, 170, 47), gamelogic)

        self.status.render(screen)
        
    # updates river scene
    def update(self, gamelogic, event):
        
        
        if gamelogic.health == 0:
            self.finished = True

        if event.type == MOUSEBUTTONDOWN and self.start and self.startbutton.collidepoint(event.pos):
            self.start = False
            self.itempicked = False

        if event.type == MOUSEBUTTONDOWN and self.finished and self.endbutton.collidepoint(event.pos):
            self.reset(gamelogic)

        self.status.update(gamelogic, event, gamelogic.getScore(), self)

        if self.speedcount%1000 == 0:
            self.speed = self.speed+1
            self.speedcount = 0

        self.speedcount = self.speedcount + 1

        if self.count%200 == 0 and not self.start:
            # Spawn item at beginning of river
            self.spawnItem((50, 280))
            self.count = 0
            
        
        self.count += 1
        for item in self.items:
            if item.rect.x+item.rect.width/2 >= self.width:
                gamelogic.health = gamelogic.health-1
                self.items.remove(item)
                gamelogic.setScore(gamelogic.getScore()-5)
            
            item.updateTouch(event)

            if self.item == None and item.touched:
                self.itempicked = True
                self.item = item
                
            
        if self.itempicked:
            if self.item.update(event, self.bins, gamelogic):
                self.draw_item = False
                self.itempicked = False
                self.items.remove(self.item)
                self.item = None