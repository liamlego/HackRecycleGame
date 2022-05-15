import pygame

class GameLogic:
    def __init__(self):
        MENU,PILE,RIVER = 0, 1, 2
        self.scene = MENU
        self.score = 0
        self.health = 3
        self.soundlevel = 3

    def getState(self):
        return self.scene

    def setState(self, state):
        self.scene = state
    
    def getScore(self):
        return self.score

    def setScore(self, score):
        self.score = score