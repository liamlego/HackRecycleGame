import pygame
import os

from status import SoundButton

class Button(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, text, fontsize):
        self.x = xpos
        self.y = ypos

        self.button_color = (0,50,128)

        # Button Text 
        self.font = pygame.font.Font('freesansbold.ttf', fontsize)
        self.textcolor = (255, 255, 255)

        self.text = self.font.render(text, True, self.textcolor)

        self.rect = self.text.get_rect()
        self.rect.center = (xpos,ypos)

        self.width = self.rect.width
        self.height = self.rect.height
        self.x = self.rect.x
        self.y = self.rect.y

    def draw(self, screen):
        pygame.draw.rect(screen, self.button_color, pygame.Rect(self.rect.x-5, self.rect.y-5, self.rect.width+10, self.rect.height+10), 0, 5)
        screen.blit(self.text, self.rect)
        
    
    def getBoundaries(self):
        return (self.x, self.y, self.width, self.height)

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
        self.hardearth = pygame.image.load(os.path.join("images", "tinyearth.png"))
        self.hearthrect = self.hardearth.get_rect()
        self.hearthrect.x, self.hearthrect.y = 1000, 630

        self.first = (self.main)
        self.second = (self.easy, self.hard)

        self.image = pygame.image.load(os.path.join("images", "menu.png"))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

        self.rect.width = renderer.width
        self.rect.width = renderer.height

        self.stage = 0

    def render(self, screen):
        screen.blit(self.image, self.rect)

       

        self.soundb.render(screen)
        #self.title.draw(screen)

        # Draw Buttons
        if self.stage == 0:
            screen.blit(self.earth, self.earthrect)
            pygame.draw.rect(screen, (0,0,0), self.main, 1)
        elif self.stage == 1:
            screen.blit(self.easyearth, self.eearthrect)
            screen.blit(self.hardearth, self.hearthrect)
            pygame.draw.rect(screen, (0,0,0), self.easy, 1)
            pygame.draw.rect(screen, (0,0,0), self.hard, 1)
            
        

    def update(self, gamelogic, event):

        self.soundb.update(gamelogic, event)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.stage == 0 and self.main.collidepoint(pygame.mouse.get_pos()):
                self.stage = 1
            elif self.stage == 1 and self.easy.collidepoint(pygame.mouse.get_pos()):
                gamelogic.setState(1)
                self.stage = 0
            elif self.stage == 1 and self.hard.collidepoint(pygame.mouse.get_pos()):
                gamelogic.setState(2)
                self.stage = 0