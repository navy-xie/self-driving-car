import pygame

class Controls:
    def __init__(self):
        self.left = False
        self.right = False
        self.forward = False
        self.reverse = False

    def update(self):
        keys = pygame.key.get_pressed()
        self.left = keys[pygame.K_LEFT]
        self.right = keys[pygame.K_RIGHT]
        self.forward = keys[pygame.K_UP]
        self.reverse = keys[pygame.K_DOWN]
