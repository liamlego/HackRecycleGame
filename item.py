import pygame
import os

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