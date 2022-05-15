import os
import pygame

class HomeButton(pygame.sprite.Sprite):

    def __init__(self, width, height):
        super().__init__()
        self.backimage = pygame.image.load(os.path.join("images", "arrow.png"))

        self.rect = self.backimage.get_rect()

        self.rect.x = 50
        self.rect.y = 50

    def render(self, screen):
        screen.blit(self.backimage, self.rect)

    def update(self, gamelogic, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            gamelogic.setState(0)

class Status:

    def __init__(self, width, height):

        self.home = HomeButton(width, height)

        self.font = pygame.font.Font('freesansbold.ttf', 40)
        self.textcolor = (255, 255, 255)

        self.text = self.font.render("0", True, self.textcolor)

        self.textrect = self.text.get_rect()

        self.textrect.x = width-100
        self.textrect.y = 50

    def render(self, screen):
        screen.blit(self.text,self.textrect)
        self.home.render(screen)
        

    def update(self, gamelogic, event, score, scene):
        self.text = self.font.render(""+str(score), True, self.textcolor)

        if event.type == pygame.MOUSEBUTTONDOWN and self.home.rect.collidepoint(event.pos):
            gamelogic.setState(0)
            scene.reset(gamelogic)
        