import pygame
from pygame.sprite import Sprite
import random


class Pirate(Sprite):

    def __init__(self, pi_game):
        super().__init__()  # Inherit from the Sprite class

        self.screen = pi_game.screen  # Instance for the game screen
        self.screen_rect = self.screen.get_rect()  # Instance for the screen's rectangle

        # Load the pirate image and set its rectangle
        self.image = pygame.image.load("pirate_ship.bmp")
        self.rect = self.image.get_rect()

        # Start each new pirate in the top right corner
        self.rect.x = 850
        self.rect.y = random.randint(0, 600)

        # Store the pirate's exact position
        self.y = float(self.rect.y)
