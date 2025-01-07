import pygame
import pygame.font


class Pause:

    def __init__(self, pi_game):
        self.screen = pi_game.screen  # Instance for the game screen
        self.screen_rect = self.screen.get_rect()  # Instance for the screen's rectangle
        self.settings = pi_game.settings  # Instance of the game settings

        # Pause settings
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 48)
        self.pause_text = "Game Paused. Press ESC to Resume."
        self.pause_image = self.font.render(self.pause_text, True, self.text_color)
        self.pause_rect = self.pause_image.get_rect()

        # Display the pause in the middle of the screen
        self.pause_rect.center = self.screen_rect.center

    def draw_pause(self):
        self.screen.blit(self.pause_image, self.pause_rect)
