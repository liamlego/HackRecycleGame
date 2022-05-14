import pygame
import os
from pygame.locals import *

class Item(pygame.sprite.Sprite):

    def __init__(self, type, size):
        super().__init__()
        self.x = 0
        self.y = 0
        self.color = (255,255,255)
        
        self.image = pygame.image.load(os.path.join("images","waterbottle.png"))
        pygame.Surface.convert_alpha(self.image)
        self.rect = self.image.get_rect()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, event):
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
            self.rect.move_ip(event.rel)