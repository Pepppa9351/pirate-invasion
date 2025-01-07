import pygame


class Porch(pygame.sprite.Sprite):

    def __init__(self, pi_game):
        super().__init__()

        self.screen = pi_game.screen  # Create an instance of the game screen
        self.settings = pi_game.settings  # Create  an instance of the game settings
        self.screen_rect = pi_game.screen.get_rect()  # Create an instance of the screen's rectangle

        # Load the image of the porch and set its size
        self.image = pygame.image.load("textures/hullSmall (1).png")
        self.image = pygame.transform.scale(self.image, (self.settings.porch_width, self.settings.porch_height))

        # Get the porch's rectangle
        self.rect = self.image.get_rect()

        # Set the porch position
        self.rect.x = -900
        self.rect.y = -400

    # Blit the porch on the screen at its set location
    def draw_porch(self):
        self.screen.blit(self.image, self.rect)
