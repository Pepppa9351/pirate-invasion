import pygame
import pygame.font


class Scoreboard:

    def __init__(self, pi_game):
        self.screen = pi_game.screen  # Create an instance of the game screen
        self.settings = pi_game.settings  # Create  an instance of the game settings
        self.screen_rect = pi_game.screen.get_rect()  # Create an instance of the screen's rectangle
        self.score = 0  # Create an instance of the game score

        # Scoreboard settings
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Get the image and its rectangle
        score_string = str(self.score)
        self.score_image = self.font.render(score_string, True, self.text_color)
        self.score_rect = self.score_image.get_rect()

        # Display the score at the top right of the screen
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def update_scoreboard(self):

        score_string = str(self.score)
        self.score_image = self.font.render(score_string, True, self.text_color)

        # Display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_scoreboard(self):
        self.screen.blit(self.score_image, self.score_rect)
