import pygame, random
import circleshape
from constants import *

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            surface = screen,
            color = pygame.Color(255,255,255),
            
            # position is a property in the parent class
            center = (self.position.x, self.position.y),

            radius = self.radius,
            width = 2
        )

    def update(self, dt):
        # velocity needs to come from the CircleShape parent class 
        # and update position
        self.position += self.velocity * dt  

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)
        # rotate() returns a new rotated vector at some angle
        velocity1 = self.velocity.rotate(random_angle)
        velocity2 = self.velocity.rotate(-random_angle)

        # calculate radius of new pieces
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Create two new asteroids with the new radius
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        asteroid1.velocity = velocity1 * 1.2
        asteroid2.velocity = velocity2 * 1.2

        # add the new asteroids to the existing group
        # calling self.Group() would create a new group, which is incorrect
        for group in self.groups():
            group.add(asteroid1, asteroid2)