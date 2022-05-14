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

"""


class Item(pygame.sprite.Sprite):

    def __init__(self, type, width, height):
        super().__init__()
        self.x = 0
        self.y = 0
        self.color = (255,255,255)
        
        self.image = 0
        self.rect = 0

        self.setImage(type, width, height)

    def setImage(self, type, width, height):

        str_img = ""

        if type == 0:
            str_img = "glass1.PNG"
        elif type == 1:
            str_img = "glass2.PNG"
        elif type == 2:
            str_img = "glass3.PNG"
        elif type == 3:
            str_img = "matal2.PNG"
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

        self.image = pygame.image.load(os.path.join("images/items", str_img))
        pygame.Surface.convert_alpha(self.image)
        self.rect = pygame.Rect(0, 0, 10, 10)


    # Set locaiton of the center of the item
    def setLocation(self, location): 
        self.rect.center = 0,0

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, event):
        
        """
        if event.type == MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.moving = True

        elif event.type == MOUSEBUTTONUP:
            # if collide with correct bin rect
                # disapear
                # increase score
            # elif
                # decrease score
                # move to bottom center of screen ??
            self.moving = False

        elif event.type == MOUSEMOTION and self.moving:
            self.rect.move_ip(event.rel)"""