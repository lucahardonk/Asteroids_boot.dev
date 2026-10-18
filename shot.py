from constants import *
from circleshape import CircleShape
import pygame

class Shot (CircleShape):
    def __init__(self, x: float, y: float, radius=SHOT_RADIUS) -> None:
        super().__init__(x , y, radius )

    def draw(self, surface: pygame.Surface, color="white", position: pygame.Vector2 = None, radius: float = SHOT_RADIUS, line_width= LINE_WIDTH) -> None:
            pygame.draw.circle(surface, "white", self.position, self.radius, LINE_WIDTH )
            
    def update(self, dt: float) -> None:
        self.position += self.velocity * dt