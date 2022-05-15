import pygame
import os
from pygame.locals import *
from status import HomeButton

class VolumeSlider(pygame.sprite.Sprite):

    def __init__(self, width, height, text):
        super().__init__()
        



class Settings:

    def __init__(self, width, height):
        self.width, self.height = width, height
        self.home = HomeButton(width, height)

    def render(self, screen):
        self.home.render(screen)
        
    # decreases size of pile
    def update(self, gamelogic, event):
        self.home.update(gamelogic, event)