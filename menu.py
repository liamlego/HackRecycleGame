import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, w, h, text, size):
        self.x = xpos
        self.y = ypos
        self.width = w
        self.height = h
        
        # Button frame
        self.image = pygame.Surface((w,h))
        self.image.fill((255,0,255))

        self.rect = self.image.get_rect()
        self.rect.center = (xpos,ypos)

        # Button Text 
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.textcolor = (255, 255, 255)

        self.text = self.font.render(text, self.textcolor, (0,0,0))

        self.textRect = text.get_rect()

        self.textRect.center = (xpos,ypos)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        screen.blit(self.text, self.textRect)

class Menu:

    def __init__(self, renderer):
        self.startgame = Button(renderer.width/2, renderer.height/2, 20, 10, "Start Game", renderer.size)
        self.credits = Button(renderer.width/2, renderer.height/2, 20, 10, "Credits", renderer.size)
        self.settings = Button(renderer.width/2, renderer.height/2, 20, 10, "Settings", renderer.size)

        self.buttons = (self.startgame, self.credits, self.settings)

        #self.image = pygame.Surface([renderer.width, renderer.height])
        #self.rect = self.image.get_rect()

    def render(self, screen):

        
        screen.blit(self.image, self.rect)

        # Draw Buttons
        for element in self.buttons:
            element.draw(screen)

    def update(self):
        x = 0