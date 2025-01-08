import pygame
import pygame.font
from button import Button


class LossMessage(Button):

    def __init__(self, pi_game, message, how_low=0):
        super().__init__(pi_game, message, how_low=0)

        # Loss message settings
        self.width = 350
        self.height = 50
        self.button_color = (101, 67, 33)

        # Build the loss message rectangle
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.rect.y = self.rect.y - how_low

        # Prepare the button
        self._prepare_message(message)
