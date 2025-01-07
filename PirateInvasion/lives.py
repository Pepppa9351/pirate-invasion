import pygame


class Lives:

    def __init__(self, pi_game):
        self.screen = pi_game.screen  # Instance for the game screen
        self.screen_rect = self.screen.get_rect()  # Instance for the screen's rectangle
        self.settings = pi_game.settings  # Instance of the game settings

        # Load the heart image and set its rectangle
        self.image = pygame.image.load("textures/heart.png")
        self.rect = self.image.get_rect()

        # Store the amount of hearts
        self.life_count = 3

        # Store the position of the first heart
        self.rect.x = self.settings.screen_width - 40
        self.rect.y = self.settings.screen_height - 40

    def draw_lives(self):
        for heart in range(0, self.life_count):

            match heart:
                case 0:
                    self.rect.x = self.settings.screen_width - 40

                case 1:
                    self.rect.x = self.settings.screen_width - 80

                case 2:
                    self.rect.x = self.settings.screen_width - 120

            self.screen.blit(self.image, self.rect)






