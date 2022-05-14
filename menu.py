import pygame
import os

class Button(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, text, fontsize):
        self.x = xpos
        self.y = ypos

        # Button Text 
        self.font = pygame.font.Font('freesansbold.ttf', fontsize)
        self.textcolor = (255, 0, 255)

        self.text = self.font.render(text, True, self.textcolor, (0,255,0))

        self.rect = self.text.get_rect()
        self.rect.center = (xpos,ypos)

        self.width = self.rect.width
        self.height = self.rect.height
        self.x = self.rect.x
        self.y = self.rect.y

    def draw(self, screen):
        screen.blit(self.text, self.rect)
    
    def getBoundaries(self):
        return (self.x, self.y, self.width, self.height)

class Menu:

    def __init__(self, renderer):

        self.title = Button(renderer.width/2, 50, "Title", 32)

        self.startgame = Button(renderer.width/2, renderer.height/2, "Easy", 24)
        self.credits = Button(renderer.width/2, renderer.height/2+30, "Hard", 24)
        self.settings = Button(renderer.width/2, renderer.height/2+60, "Settings", 24)

        self.buttons = (self.startgame, self.credits, self.settings)

        self.image = pygame.Surface([40, 40])
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

        self.rect.width = 640
        self.rect.width = 400

    def render(self, screen):

        screen.blit(self.image, self.rect)

        self.title.draw(screen)
        # Draw Buttons
        for element in self.buttons:
            element.draw(screen)
        

    def update(self, gamelogic, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            it = 0
            for button in self.buttons:
                if button.rect.collidepoint(pygame.mouse.get_pos()):
                    if it == 0:
                        gamelogic.setState(1)
                    elif it == 1:
                        gamelogic.setState(2)
                    elif it == 2:
                        gamelogic.setState(3)
                it = it + 1