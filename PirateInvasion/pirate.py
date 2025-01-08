import pygame
import random


class Pirate(pygame.sprite.Sprite):

    def __init__(self, pi_game):
        super().__init__()  # Inherit from the Sprite class

        self.screen = pi_game.screen  # Instance for the game screen
        self.screen_rect = self.screen.get_rect()  # Instance for the screen's rectangle
        self.settings = pi_game.settings  # Instance of the game settings

        # Load the pirate image and set its rectangle
        self.image = pygame.image.load("textures/ship (2).png")
        self.image = pygame.transform.rotate(self.image, 270)
        self.rect = self.image.get_rect()

        # Start in a random position out of the map
        self.rect.x = self.screen_rect.right
        self.rect.y = random.randint(0, self.screen_rect.height - 100)

        # Create a float value of the pirate's vertical position
        self.y = float(self.rect.y)

        # Create a float value of the pirate's horizontal position
        self.x = float(self.rect.x)

    # Move and update the pirate's position
    def update(self):
        # Move the bullet at the distance of the bullet speed each frame
        self.x -= self.settings.pirate_speed

        # Update the rect position of the bullet
        self.rect.x = int(self.x)
