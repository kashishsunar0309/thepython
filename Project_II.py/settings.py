class Settings:
    "A Class to store all settings for Alien Invasion"
    def __init__(self):
        #Initialize the game's settings.
        #Screen settings
        self.screen_width = 1080
        self.screen_height = 800
        self.bg_color = (255,255,255)
        #ship Settings
        self.ship_speed = 2.5
        #Bullet Setttings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)