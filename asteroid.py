import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        pygame.sprite.Sprite.kill(self)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        random_angle = random.uniform(20, 50)
        new_vector_one = self.velocity.rotate(random_angle)
        new_vector_two = self.velocity.rotate(-random_angle)
        new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_child_one = Asteroid(
            self.position.x, self.position.y, new_asteroid_radius
        )
        asteroid_child_two = Asteroid(
            self.position.x, self.position.y, new_asteroid_radius
        )
        asteroid_child_one.velocity = new_vector_one * 1.2
        asteroid_child_two.velocity = new_vector_two * 1.2
