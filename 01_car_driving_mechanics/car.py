import pygame
import math
from pygame import Surface

from controls import Controls


class Car:
    def __init__(
        self,
        center_x: float = 0,
        center_y: float = 0,
        width: float = 0,
        height: float = 0,
    ):
        self.center_x = center_x
        self.center_y = center_y
        self.width = width
        self.height = height

        self.speed = 0
        self.angle = 0
        self.acceleration = 0.2
        self.max_speed = 3
        self.friction = 0.05
        self.turning_speed = 3

        self.controls = Controls()

        image = pygame.image.load("../car.png")
        self.image = pygame.transform.scale(image, (self.width, self.height))

    def copy_from(self, other: "Car"):
        self.center_x = other.center_x
        self.center_y = other.center_y
        self.width = other.width
        self.height = other.height
        self.speed = other.speed
        self.angle = other.angle
        self.acceleration = other.acceleration
        self.max_speed = other.max_speed
        self.friction = other.friction
        self.turning_speed = other.turning_speed

    def store(self):
        self.copy = Car()
        self.copy.copy_from(self)

    def reset(self):
        self.copy_from(self.copy)
        self.controls.reset()

    def draw(self, surface: Surface):
        image = pygame.transform.rotate(self.image, self.angle)
        surface.blit(
            image,
            (self.center_x - self.width / 2, self.center_y - self.height / 2),
        )

    def update(self):
        self.move()

    def move(self):
        self.controls.update()

        # forward and reverse movement
        if self.controls.forward:
            self.speed += self.acceleration
        if self.controls.reverse:
            self.speed -= self.acceleration

        # speed limits
        if self.speed > self.max_speed:
            self.speed = self.max_speed
        if self.speed < -self.max_speed / 2:
            self.speed = -self.max_speed / 2

        # speed adjustment
        if self.speed > 0:
            self.speed -= self.friction
        if self.speed < 0:
            self.speed += self.friction
        if abs(self.speed) < self.friction:
            self.speed = 0

        # left and right movement
        if self.speed != 0:
            flip = 1 if self.speed > 0 else -1
            deviation = self.turning_speed * flip
            if self.controls.left:
                self.angle += deviation
            if self.controls.right:
                self.angle -= deviation

        # update position
        angle_rad = math.radians(self.angle)
        self.center_x -= self.speed * math.sin(angle_rad)
        self.center_y -= self.speed * math.cos(angle_rad)
