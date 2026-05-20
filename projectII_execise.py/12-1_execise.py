import sys 
import pygame
class BlueSky:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        #Screen size
        self.screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption("Bluesky")
        #RGB COLOR CODE
        self.bg_color = (0,0,255)
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)
            pygame.display.flip()
            self.clock.tick(60)
if __name__ == "__main__":
    sky = BlueSky()
    sky.run()