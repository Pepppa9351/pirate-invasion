class Settings:

    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (135, 206, 235)

        # Player settings
        self.player_speed = 5
        self.player_width = 100
        self.player_height = 50

        # Bullet settings
        self.bullet_speed = 5
        self.bullet_color = (60, 60, 60)
        self.bullet_width = 20
        self.bullet_height = 20
        self.bullets_allowed = 10

        # Pirate settings
        self.pirate_speed = 5
        self.pirate_cooldown = 2000
