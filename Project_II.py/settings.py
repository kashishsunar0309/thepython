class Settings:
    "A Class to store all settings for Alien Invasion"
    def __init__(self):
        #Initialize the game's settings.
        #Screen settings
        self.screen_width = 1080
        self.screen_height = 800
        self.bg_color = (255,255,255)
        #ship Settings
        self.ship_limit = 3
        #Bullet Setttings
        self.bullet_width = 3
        self.bullet_height = 20
        self.bullet_color = (255,0,0)
        self.bullets_allowed = 9
        self.fleet_drop_speed = 10
        self.speedup_scale = 1.5
        #How quickly the alien point values increase.
        self.score_scale = 1.5
    def initialize_dynamic_settinngs(self):
        self.ship_speed = 7.0
        self.bullet_speed = 3.5
        #Alien settings
        self.alien_speed = 2
        #Fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        #Scoring settings.
        self.alien_points = 50
    def increase_speed(self):
        #Increase speed settings.
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)