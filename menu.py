import pygame
import os

from status import SoundButton

class Menu:

    def __init__(self, renderer):

        self.soundb = SoundButton(renderer.width, renderer.height)
        self.main = pygame.Rect(1000, 540, 200, 200)
        self.easy = pygame.Rect(1050, 480, 100, 100)
        self.hard = pygame.Rect(1050, 680, 100, 100)

        self.earth = pygame.image.load(os.path.join("images", "earth.png"))
        self.earthrect = self.earth.get_rect()
        self.earthrect.x, self.earthrect.y = 900, 430

        self.easyearth = pygame.image.load(os.path.join("images", "tinyearth.png"))
        self.eearthrect = self.easyearth.get_rect()
        self.eearthrect.x, self.eearthrect.y = 1000, 430

        self.font = pygame.font.Font('freesansbold.ttf', 40)

        self.easytext = self.font.render("Easy", True, (255, 255, 255))
        self.easytextrect = self.easytext.get_rect()
        self.easytextrect.x, self.easytextrect.y = 1054, 518

        

        self.hardearth = pygame.image.load(os.path.join("images", "tinyearth.png"))
        self.hearthrect = self.hardearth.get_rect()
        self.hearthrect.x, self.hearthrect.y = 1000, 630

        self.hardtext = self.font.render("Hard", True, (255, 255, 255))
        self.hardtextrect = self.hardtext.get_rect()
        self.hardtextrect.x, self.hardtextrect.y = 1054, 718

        self.first = (self.main)
        self.second = (self.easy, self.hard)

        self.image = pygame.image.load(os.path.join("images", "menu.png"))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

        self.rect.width = renderer.width
        self.rect.width = renderer.height

        self.stage = 0

    def click(self):
        pygame.mixer.music.load("sounds/blipSelect.wav")
        pygame.mixer.music.play()


    def render(self, screen):
        self.soundb.render(screen)

        # Draw Buttons
        if self.stage == 0:
            screen.blit(self.earth, self.earthrect)
        elif self.stage == 1:
            screen.blit(self.easyearth, self.eearthrect)
            screen.blit(self.easytext, self.easytextrect)
            screen.blit(self.hardearth, self.hearthrect)
            screen.blit(self.hardtext, self.hardtextrect)
        

    def update(self, gamelogic, event):

        self.soundb.update(gamelogic, event)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.stage == 0 and self.main.collidepoint(pygame.mouse.get_pos()):
                self.click()
                self.stage = 1
            elif self.stage == 1 and self.easy.collidepoint(pygame.mouse.get_pos()):
                gamelogic.setState(1)
                self.click()
                self.stage = 0
            elif self.stage == 1 and self.hard.collidepoint(pygame.mouse.get_pos()):
                gamelogic.setState(2)
                self.click()
                self.stage = 0