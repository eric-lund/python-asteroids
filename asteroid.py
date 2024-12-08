import circleshape
import pygame

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

    