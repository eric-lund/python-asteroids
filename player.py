import circleshape
import pygame
from  constants import *
from shot import Shot

class Player(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(
            screen, 
            pygame.Color(255,255,255), 
            self.triangle(), 
            width = 2
            )
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

        # decrease the time when update() is called
        self.timer -= dt

    def move(self, dt):
        # Start with a unit vector of (0,1) and rotate by the player's rotation
        forward = pygame.Vector2(0, 1).rotate(self.rotation)

        # add the vector to the position; larger vector -> faster movement
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self): 
        # do not shoot if there is time left
        if self.timer > 0:
            return

        self.timer = PLAYER_SHOOT_COOLDOWN
        forward = self.triangle()
        shot = Shot(forward[0].x, forward[0].y, SHOT_RADIUS)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation)
        shot.velocity *= PLAYER_SHOOT_SPEED