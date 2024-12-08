# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame, sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

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
    asteroids = pygame.sprite.Group()
    asteroidfield = pygame.sprite.Group()   

    # Add static field to class
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (asteroidfield, updatable)

    # Create objects after creating static field to inherit changes
    player = Player(x, y)
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   #makes the window's close button work
                return
        dt = clock.tick(60) / 1000

        pygame.Surface.fill(screen, color='#000000') # black background
        
        # iterate over the groups instead of coding each class
        for draw in drawable:
            draw.draw(screen)

        for update in updatable:
            update.update(dt)

        # check if the player hits an asteroid
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                sys.exit()

        pygame.display.flip()




# ensures the main() function is only called when this file is run directly
# won't run as a package
# part of the "pythonic" way
if __name__ == "__main__":
    main()