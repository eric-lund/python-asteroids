# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame, sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()  #initialize pygame
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    clock = pygame.time.Clock()
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    # Create groups
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    asteroidfield = pygame.sprite.Group()
    shots = pygame.sprite.Group() 

    # Add static field to class
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (asteroidfield, updateable)
    # add Shot class to shots, updateable, and drawable groups
    Shot.containers = (shots, updateable, drawable)

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

        for update in updateable:
            update.update(dt)

        # check if the player hits an asteroid
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if shot.collision(asteroid):
                    # kill() is part of pygame removing objects from groups
                    shot.kill()
                    # call split() to divide larger asteroids
                    asteroid.split()

        pygame.display.flip()

# ensures the main() function is only called when this file is run directly
# won't run as a package
# part of the "pythonic" way
if __name__ == "__main__":
    main()