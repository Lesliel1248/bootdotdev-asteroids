# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    # Initialize pygame
    pygame.init()

    # Create the window with our predefined screen size
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Game loop
    while True:
        # Check for window close events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Fill the screen black (RGB color black is (0, 0, 0))
        screen.fill((0, 0, 0))

        # Refresh the display
        pygame.display.flip()
        
if __name__ == "__main__":
    main()