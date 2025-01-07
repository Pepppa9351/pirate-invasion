import pygame.font


class Settings:

    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800

        # Player settings
        self.player_speed = 5
        self.player_width = 70
        self.player_height = 35

        # Bullet settings
        self.bullet_speed = 5
        self.bullet_width = 20
        self.bullet_height = 20
        self.bullets_allowed = 5

        # Pirate settings
        self.pirate_speed = 3
        self.pirate_cooldown = 2000
        self.pirate_speed_up = 1.05

        # Porch settings
        self.porch_width = 1000
        self.porch_height = 2000

