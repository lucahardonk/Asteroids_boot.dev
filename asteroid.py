from  circleshape import CircleShape
from  constants import *
import pygame
import random
from logger import log_event

class Asteroid (CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, surface: pygame.Surface, color="white", position: pygame.Vector2 = None, radius: float = 0, line_width= LINE_WIDTH) -> None:
            pygame.draw.circle(surface, "white", self.position, self.radius, LINE_WIDTH )
            
    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self ) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            random_angle = pygame.math.Vector2(1, 0).rotate(random.uniform(20, 50))
            mirrored_random_angle = random_angle*-1
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asterod1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteriod2 = Asteroid(self.position.x, self.position.y, new_radius)
            asterod1.velocity = random_angle * self.velocity.length() * 1.2
            asteriod2.velocity = mirrored_random_angle * self.velocity.length() * 1.2
