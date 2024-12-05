# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    pygame.init  #initialize pygame
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   #makes the window's close button work
                return    
        dt = clock.tick(60) / 1000
        
        pygame.Surface.fill(screen, color='#000000') # black background
        pygame.display.flip()


# ensures the main() function is only called when this file is run directly
# won't run as a package
# part of the "pythonic" way
if __name__ == "__main__":
    main()