import pygame


class Bullet(pygame.sprite.Sprite):

    def __init__(self, pi_game):
        super().__init__()  # Inherit from the Sprite class

        self.screen = pi_game.screen  # Instance of the game screen
        self.settings = pi_game.settings  # Instance of the game settings

        # Load the bullet image and get its rectangle
        self.image = pygame.image.load("textures/cannonBall.png")
        self.image = pygame.transform.scale(self.image, (self.settings.bullet_width, self.settings.bullet_height))
        self.rect = self.image.get_rect()
        self.rect.midleft = pi_game.player.rect.midright

        # Create a float value of the bullet's position
        self.x = float(self.rect.x)

    # Move and update the bullet's position
    def update(self):

        # Move the bullet at the distance of the bullet speed each frame
        self.x += self.settings.bullet_speed

        # Update the rect position of the bullet
        self.rect.x = int(self.x)






