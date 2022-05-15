import pygame
import os
from pygame.locals import *

"""
Item Key values:

0: glass1.PNG
1: glass2.PNG
2: glass3.PNG
3: matal2.PNG
4: metal1.PNG
5: metal3.PNG
6: paper1.PNG
7: paper2.PNG
8: paper3.PNG
9: plastic1.PNG
10: plastic2.PNG
11: plastic3.PNG
12: trash1.PNG
13: trash2.PNG
14: trash3.PNG

"""


class Item(pygame.sprite.Sprite):

    def __init__(self, type, location):
        super().__init__()

        self.bintype = int(type / 3)
        
        self.image = 0
        self.rect = 0
        self.x, self.y = 0, 0
        self.moving = False

        self.picked = False

        self.speed = 0

        self.setImage(type, location)

    # loads correct image based on given type at given location
    def setImage(self, type, location):

        str_img = ""

        if type == 0:
            str_img = "glass1.PNG"
        elif type == 1:
            str_img = "glass2.PNG"
        elif type == 2:
            str_img = "glass3.PNG"
        elif type == 3:
            str_img = "metal2.PNG"
        elif type == 4:
            str_img = "metal1.PNG"
        elif type == 5:
            str_img = "metal3.PNG"
        elif type == 6:
            str_img = "paper1.PNG"
        elif type == 7:
            str_img = "paper2.PNG"
        elif type == 8:
            str_img = "paper3.PNG"
        elif type == 9:
            str_img = "plastic1.PNG"
        elif type == 10:
            str_img = "plastic2.PNG"
        elif type == 11:
            str_img = "plastic3.PNG"
        elif type == 12:
            str_img = "trash1.PNG"
        elif type == 13:
            str_img = "trash2.PNG"
        elif type == 14:
            str_img = "trash3.PNG"

        self.image = pygame.image.load(os.path.join("images/items", str_img))
        pygame.Surface.convert_alpha(self.image)
        self.rect = self.image.get_rect()
        self.x, self.y = location
        self.setLocation(location)


    # Set locaiton of the center of the item
    def setLocation(self, location): 
        self.rect.center = location
        self.x, self.y = location

    def moveWithSpeed(self):
        if not self.picked:
            self.rect.x += self.speed

    def setSpeed(self, speed):
        self.speed = speed

    def getLocation(self):
        return (self.rect.x, self.rect.y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    # updates item based on mouse input
    def update(self, event, bins, gamelogic):
        
        # if item and mouse are in same location while mousebutton down
        if event.type == MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.moving = True
                self.picked = True

        # if item is released
        elif event.type == MOUSEBUTTONUP and self.picked:
            touched = False
            for bin in bins.getBins():
                
                # if item is over bin
                if bin.collision_rect.colliderect(self.rect):
                    
                    # if correct bin, increase score & eat item
                    if self.bintype == bin.type:
                        touched = True
                        bin.eat()
                        gamelogic.setScore(gamelogic.getScore() + 20)
                        return True
                    
                    # if incorrect bin, decrease score
                    else:
                        gamelogic.setScore(gamelogic.getScore() - 20)
                        bin.bad()

            # if item not over correct bin move to center bottom
            if not touched:
                self.setLocation((700,775))
                
            self.moving = False

        # item follows mouse if item should be moving
        elif event.type == MOUSEMOTION and self.moving:
            self.rect.move_ip(event.rel)