# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():
    pygame.init  #initialize pygame
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    clock = pygame.time.Clock()
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    # Create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # Add static field to Player class
    Player.containers = (updatable, drawable)

    # Create Player objects after creating static
    player = Player(x, y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   #makes the window's close button work
                return
        dt = clock.tick(60) / 1000

        pygame.Surface.fill(screen, color='#000000') # black background
        # player.draw(screen)
        # player.update(dt)
        for draw in drawable:
            draw.draw(screen)

        for update in updatable:
            update.update(dt)

        pygame.display.flip()




# ensures the main() function is only called when this file is run directly
# won't run as a package
# part of the "pythonic" way
if __name__ == "__main__":
    main()