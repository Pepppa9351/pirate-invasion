import sys
import pygame
from settings import Settings
from player import Player
from bullet import Bullet
from pirate import Pirate
from porch import Porch
from scoreboard import Scoreboard
from lives import Lives
from pause import Pause


class PirateInvasion:

    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()  # Instance of clock to control the frame rate
        self.settings = Settings()  # Instance of settings
        self.last_pirate_spawn = 0  # Instance to save time for the pirate spawn
        self.pause = False  # Instance of the game pause state

        # Sets the screen width and height from settings
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        # Create an instance of the screen's rectangle
        self.screen_rect = self.screen.get_rect()

        # Sets the window title
        pygame.display.set_caption("Pirate Invasion")

        # Set the background texture image
        self.background_texture = pygame.image.load("textures/tile_73.png")
        self.background_texture = pygame.transform.scale(self.background_texture,
                                                         (self.settings.screen_width, self.settings.screen_height))

        self.player = Player(self)  # Instance of the player
        self.bullets = pygame.sprite.Group()  # Instance for active bullets
        self.pirates = pygame.sprite.Group()  # Instance for alive pirates
        self.porch = Porch(self)  # Instance of the porch
        self.scoreboard = Scoreboard(self)  # Instance of the scoreboard
        self.lives = Lives(self)  # Instance of the lives
        self.pausing = Pause(self)  # Instance of the pause

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
        elif event.key == pygame.K_ESCAPE:
            if not self.pause:
                self.pause = True
                print("pause")
            else:
                self.pause = False
                print("unpause")

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

    def _update_scoreboard(self):

        # Check for pirate's collision with bullets, add 100 score for every collision
        if pygame.sprite.groupcollide(self.bullets, self.pirates, True, True):
            self.scoreboard.score += 100
            self.settings.pirate_speed *= self.settings.pirate_speed_up
            print("Enemy hit!")

        # Get the string of the score
        score_string = str(self.scoreboard.score)

        # Get the image of the scoreboard
        self.scoreboard.score_image = self.scoreboard.font.render(score_string, True, self.scoreboard.text_color)

        # Display the score at the top right of the screen
        self.scoreboard.score_rect = self.scoreboard.score_image.get_rect()
        self.scoreboard.score_rect.right = self.screen_rect.right - 20
        self.scoreboard.score_rect.top = 20

        # Blit the current score on the screen
        self.scoreboard.show_scoreboard()

    # Draw the current amount of lives
    def _update_lives(self):

        # Check for collision with the porch
        if pygame.sprite.spritecollide(self.porch, self.pirates, True):
            print("Porch hit!")
            self.lives.life_count -= 1

            # Draw the remaining lives
            self.lives.draw_lives()

        # Check if there are still lives left
        if self.lives.life_count <= 0:
            sys.exit()

    # Add each new pirate to the fleet
    def _spawn_pirate(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_pirate_spawn > 2000:
            pirate = Pirate(self)
            self.pirates.add(pirate)
            self.last_pirate_spawn = current_time  # Reset the timer after spawning

    # Update everything on the screen to the latest state
    def _update_screen(self):

        # Fill the screen with the color set in settings
        self.screen.blit(self.background_texture, (0, 0))

        # Draw the porch on the screen
        self.porch.draw_porch()

        # Draw the player in its current location
        self.player.draw_player()

        # Draw each pirate in the pirate group
        self.pirates.draw(self.screen)

        # Draw each bullet in the bullets group
        self.bullets.draw(self.screen)

        # Draw the scoreboard
        self._update_scoreboard()

        # Draw the remaining lives
        self.lives.draw_lives()

        # Updates the display to the latest screen
        pygame.display.flip()

    # The mainloop of the game
    def run_game(self):
        while True:
            self._check_events()

            if self.pause:
                self.pausing.draw_pause()
                pygame.display.flip()

            else:
                self.player.update_player()
                self._update_bullets()
                self._update_lives()
                self.pirates.update()
                self._spawn_pirate()
                self._update_screen()
                self.clock.tick(60)


if __name__ == '__main__':
    pi = PirateInvasion()  # Create an instance of the game
    pi.run_game()  # Start the game
