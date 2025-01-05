import sys
import pygame
from settings import Settings
from player import Player
from bullet import Bullet
from pirate import Pirate


class PirateInvasion:

    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()  # Instance of clock to control the frame rate
        self.settings = Settings()  # Instance of settings
        self.last_pirate_spawn = 0  # Instance to save time for the pirate spawn

        # Sets the screen width and height from settings
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        # Create an instance of the screen's rectangle
        self.screen_rect = self.screen.get_rect()

        # Sets the window title
        pygame.display.set_caption("Pirate Invasion")

        self.player = Player(self)  # Instance of the player
        self.bullets = pygame.sprite.Group()  # Instance for active bullets
        self.pirates = pygame.sprite.Group()  # Instance for alive pirates


    # Check for events in the game
    def _check_events(self):
        for event in pygame.event.get():

            # If the event is game quitting, exit the game
            if event.type == pygame.QUIT:
                sys.exit()

            # If the event is pressing down a key, check which key it is
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            # If the event is letting go off a key, check which key it is
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    # Checks which key we pressed
    def _check_keydown_events(self, event):
        if event.key == pygame.K_w:
            self.player.moving_up = True
        elif event.key == pygame.K_s:
            self.player.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    # Checks which key we let go off
    def _check_keyup_events(self, event):
        if event.key == pygame.K_w:
            self.player.moving_up = False
        elif event.key == pygame.K_s:
            self.player.moving_down = False

    # Create a new bullet and add it to the group of bullets
    def _fire_bullet(self):

        # Check if there are fewer bullets than the maximum amount allowed
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)

            # noinspection PyTypeChecker
            # Add the new bullet to the group
            self.bullets.add(new_bullet)

    # Update the position of the bullets and delete the ones that are off the screen
    def _update_bullets(self):

        # Update each bullets position
        self.bullets.update()

        # Check if each bullet isn't over the edge of the screen
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.screen_rect.right:
                self.bullets.remove(bullet)
            #  print(len(self.bullets))

    # Add each new pirate to the fleet
    def _spawn_pirate(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_pirate_spawn > 2000:
            pirate = Pirate(self)
            self.pirates.add(pirate)
            self.last_pirate_spawn = current_time  # Reset the timer after spawning

    # Update pirate's position and check if they haven't been hit
    def _update_pirates(self):
        pass

    # Update everything on the screen to the latest state
    def _update_screen(self):

        # Fill the screen with the color set in settings
        self.screen.fill(self.settings.bg_color)

        # For each bullet in the group of bullet, draw it
        for bullet in self.bullets.copy():
            bullet.draw_bullet()

        # Draw the ship in its current location
        self.player.draw_player()

        # Each pirate in the pirate group
        self.pirates.draw(self.screen)

        # Updates the display to the latest screen
        pygame.display.flip()

    # The mainloop of the game
    def run_game(self):
        while True:
            self._check_events()
            self.player.update_player()
            self._update_bullets()
            self._update_screen()
            self._spawn_pirate()
            self.clock.tick(60)


if __name__ == '__main__':
    pi = PirateInvasion()  # Create an instance of the game
    pi.run_game()  # Start the game
