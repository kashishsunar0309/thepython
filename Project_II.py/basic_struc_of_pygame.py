#import sys #This for the screen of the pygame code which we most memoraize and but not all
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