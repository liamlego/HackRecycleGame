import os
import pygame

class HomeButton(pygame.sprite.Sprite):

    def __init__(self, width, height):
        super().__init__()
        self.backimage = pygame.image.load(os.path.join("images", "arrow.png"))

        self.rect = self.backimage.get_rect()

        self.rect.x = 25
        self.rect.y = 25

    def render(self, screen):
        screen.blit(self.backimage, self.rect)

    def update(self, gamelogic, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            gamelogic.setState(0)

class SoundButton(pygame.sprite.Sprite):

    def __init__(self, width, height):
        super().__init__()
        
        self.backimage = pygame.image.load(os.path.join("images", "soundbig.png"))

        self.rect = self.backimage.get_rect()

        self.rect.x = width-125
        self.rect.y = height-100

    def setImage(self, path):
        self.backimage = pygame.image.load(os.path.join("images", path))

    def render(self, screen):
        screen.blit(self.backimage, self.rect)

    def update(self, gamelogic, event):

        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            gamelogic.soundlevel = (gamelogic.soundlevel+1)%4
        
        if gamelogic.soundlevel == 0:
            self.setImage("soundsmall.png")
            pygame.mixer.music.set_volume(.33)
            pygame.mixer.Channel(0).set_volume(.33)
        elif gamelogic.soundlevel == 1:
            self.setImage("soundmedium.png")
            pygame.mixer.music.set_volume(.67)
            pygame.mixer.Channel(0).set_volume(.67)
        elif gamelogic.soundlevel == 2:
            self.setImage("soundbig.png")
            pygame.mixer.music.set_volume(1)
            pygame.mixer.Channel(0).set_volume(1)
        elif gamelogic.soundlevel == 3:
            self.setImage("soundmute.png")
            pygame.mixer.music.set_volume(0)
            pygame.mixer.Channel(0).set_volume(0)

class Heart:

    def __init__(self, x, y, heartvalue):
        self.heartimage = pygame.image.load(os.path.join("images", "heart.png"))
        self.heartrect = self.heartimage.get_rect()
        
        self.heartrect.x = x
        self.heartrect.y = y

        self.should_draw = True
        self.heartvalue = heartvalue
    
    def render(self, screen):
        screen.blit(self.heartimage, self.heartrect)
        

    def update(self, gamelogic):
        if gamelogic.health >= self.heartvalue and gamelogic.getState() == 2:
            self.should_draw = True
            # if last heart, WIGGLE
            if gamelogic.health == 1:
                if self.heartrect.x < 1210:
                    self.heartrect.move_ip(1, 0)
                elif self.heartrect.x > 1190:
                    self.heartrect.move_ip(-1, 0)
        else:
            self.should_draw = False

class Status:

    def __init__(self, width, height):

        self.home = HomeButton(width, height)
        self.sound = SoundButton(width, height)

        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.textcolor = (255, 255, 255)

        self.text = self.font.render("0", True, self.textcolor)

        self.textrect = self.text.get_rect()

        self.textrect.x = width-100
        self.textrect.y = 50

        self.heart1 = Heart(width - 300, 40, 3)
        self.heart2 = Heart(width - 250, 40, 2)
        self.heart3 = Heart(width - 200, 40, 1)

        self.hearts = [self.heart1, self.heart2, self.heart3]

    def render(self, screen):
        screen.blit(self.text,self.textrect)
        self.home.render(screen)
        self.sound.render(screen)

        for heart in self.hearts:
            if heart.should_draw:
                heart.render(screen)
    
    def click(self):
        pygame.mixer.music.load("sounds/blipSelect.wav")
        pygame.mixer.music.play()
        
    def moveScore(self, x, y):
        self.textrect.x = x
        self.textrect.y = y
    
    def colorScore(self, color, gamelogic):
        self.textcolor = color
        self.text = self.font.render(str(gamelogic.getScore()), True, self.textcolor)

    def update(self, gamelogic, event, score, scene):
        for heart in self.hearts:
            heart.update(gamelogic)

        self.text = self.font.render(""+str(score), True, self.textcolor)
        self.sound.update(gamelogic, event)

        if event.type == pygame.MOUSEBUTTONDOWN and self.home.rect.collidepoint(event.pos):
            self.click()
            gamelogic.setState(0)
            scene.reset(gamelogic)
        