import pygame
import random
from circleshape import CircleShape
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self,dt):
        self.position += self.velocity * dt

    def split(self):

        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        ast_1_velocity = self.velocity.rotate(angle)
        ast_2_velocity = self.velocity.rotate(-angle)
        new_ast_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_ast_radius)
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_ast_radius)
        asteroid_1.velocity = ast_1_velocity * 1.2
        asteroid_2.velocity = ast_2_velocity * 1.2