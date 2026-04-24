class GameStats:
    #Track statistics for Alien Invasion.
    def __init__(self,ai_game):
        #Initialize statistics.
        self.settings = ai_game.settings
    def reset_stats(self):
        #Initalize statistics that can change during the game.
        self.ship_left = self.settings.ship_limit