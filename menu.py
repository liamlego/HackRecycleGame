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

        #self.title = Button(renderer.width/2, 50, "Recycle Rush", 100)

        self.easy = Button(renderer.width/2, renderer.height/2, "Easy", 50)
        self.hard = Button(renderer.width/2, renderer.height/2+100, "Hard", 50)
        self.soundb = SoundButton(renderer.width, renderer.height)
        self.main = pygame.Rect(1000, 530, 250, 250)

        self.buttons = (self.easy, self.hard)

        self.image = pygame.image.load(os.path.join("images", "menu.png"))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

        self.rect.width = renderer.width
        self.rect.width = renderer.height

    def render(self, screen):
        screen.blit(self.image, self.rect)

        self.soundb.render(screen)
        pygame.draw.rect(screen, (0,0,0), self.main, 1)
        #self.title.draw(screen)
        # Draw Buttons
        for element in self.buttons:
            element.draw(screen)
        

    def update(self, gamelogic, event):

        self.soundb.update(gamelogic, event)

        if event.type == pygame.MOUSEBUTTONDOWN:
            it = 0
            for button in self.buttons:
                if button.rect.collidepoint(pygame.mouse.get_pos()):
                    if it == 0:
                        gamelogic.setState(1)
                    elif it == 1:
                        gamelogic.setState(2)
                it = it + 1