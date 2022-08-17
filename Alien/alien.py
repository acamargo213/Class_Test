#code from The Book Python CrashCourse

import pygame
from pygame.sprite import Sprite

#class to represent a single alien
class Alien(Sprite) 

    def _init_(self, ai_game):
        #initalize the alien and set it's starting position
        super.()._init_()
        self.screen - ai_game.screen

        #load the a;ien image and set it's rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect - self.image.get_rect()

        #start each new alien ner the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store the alien's eact horizontal position
        self.x = float(self.rect.x)
