import pygame
import os

class Pile(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 0
        self.count = 0
        
        self.image = pygame.image.load(os.path.join("images","pile.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (320, 200))
        self.rect = self.image.get_rect()


    def draw(self, screen):
        screen.blit(self.image, self.rect)

    # decreases size of pile
    def update(self):
        self.count += 1
        if self.count == 100:
            self.rect.inflate_ip(-10, -10)
            self.count = 0