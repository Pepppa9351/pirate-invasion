import sys
import pygame
from settings import Settings

class PirateInvasion:

    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock() # Instance of clock to control the frame rate
        self.settings = Settings() # Instance of settings

        # Sets the screen width and height from settings
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        # Sets the window title
        pygame.display.set_caption("Pirate Invasion")

    # Check for events in the game
    def _check_events(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

    # Update everything on the screen to the latest state
    def _update_screen(self):

        # Fill the screen with the color set in settings
        self.screen.fill(self.settings.bg_color)

        # Updates the display to the latest screen
        pygame.display.flip()


     # The mainloop of the game
    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)


if __name__ == '__main__':
    pi = PirateInvasion() # Create an instance of the game
    pi.run_game() # Start the game




