"""import sys #This for the screen of the pygame code which we most memoraize and but not all
import pygame
class AlienInvasion:
    #Over all class to manage game assets and behavior.
    def __init__(self):
        #Initialize the game, and creates game resources.
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1400,800))
        pygame.display.set_caption("AlienInvasion")
        #Set the background color.
        self.bg_color = (255,0,0)
    def run_game(self):
        #Start the main loop for game.
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    #Redraw the screen during each pass through the loop.
            self.screen.fill(self.bg_color)
            pygame.display.flip()
            self.clock.tick(60)
if __name__ == "__main__":
    #Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
"""
#that another example of for display of like the first one comment code of top
#but here is new file from there i import that settings as you can see in line 3.
import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    def __init__(self):
        # Initialize the game, and create game resources
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

    def run_game(self):
        while True:
            # Watch for keyboard and mouse events
            self._check_events()
            self._update_screen()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen each pass through the loop
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # Make the most recently drawn screen visible
            pygame.display.flip()
            self.clock.tick(60)
    def _check_events(self):
        "Respond to keypresses and mouse events."
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        #Move the ship to the right.
                        self.ship.rect.x +=1
    def _update_screen(self):
        "Update images on the screen, and flip to the new screen."
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()
                
if __name__ == "__main__":
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
