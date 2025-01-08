import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self, pi_game):
        super().__init__()  # Inherit from Sprite

        self.screen = pi_game.screen  # Create an instance of the game screen
        self.settings = pi_game.settings  # Create  an instance of the game settings
        self.screen_rect = pi_game.screen.get_rect()  # Create an instance of the screen's rectangle

        # Load the image of the player and set its size
        self.image = pygame.image.load("textures/cannonMobile.png")
        self.image = pygame.transform.scale(self.image, (self.settings.player_width, self.settings.player_height))

        # Get the player's rectangle
        self.rect = self.image.get_rect()

        # Start the player at the left bottom corner of the screen
        self.rect.midleft = self.screen_rect.midleft

        # Store the location of the player
        self.y = float(self.rect.y)

        # Define boolean values of moving right and down
        self.moving_up = False
        self.moving_down = False

    # Update player's position every frame if we are holding down a key
    def update_player(self):
        if self.moving_up and self.rect.top >= 0:
            self.rect.y -= self.settings.player_speed

        elif self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.rect.y += self.settings.player_speed

        self.y = float(self.rect.y)

    # Blit the player on the screen at its current location
    def draw_player(self):
        self.screen.blit(self.image, self.rect)
