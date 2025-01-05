import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):

    def __init__(self, pi_game):
        super().__init__()  # Inherit from the Sprite class

        self.screen = pi_game.screen  # Instance of the game screen
        self.settings = pi_game.settings  # Instance of the game settings
        self.color = self.settings.bullet_color  # Instance of the bullet color

        # Create a bullet rect at 0, 0 and then set the correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = pi_game.player.rect.midright

        # Create a float value of the bullet's position
        self.x = float(self.rect.x)

    # Move and update the bullet's position
    def update(self):

        # Move the bullet at the distance of the bullet speed each frame
        self.x += self.settings.bullet_speed

        # Update the rect position of the bullet
        self.rect.x = int(self.x)

    # Draw the bullet on the screen
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)






