from .component import Component
import pygame


class StaticSpriteComponent(Component):

    def __init__(self, asset_file_name):
        self.asset_file_name = asset_file_name
        self.image = None
        # reference to the origin (upper left corner)
        self.x = 0
        self.y = 0
        # speed of movement along the axes (x and y)
        self.vx = 0.1
        self.vy = 0.1

    def load(self):
        self.image = pygame.image.load(self.asset_file_name)

    def render(self):
        rect = self.image.get_rect()
        rect.centerx = self.x
        rect.centery = self.y

    def update(self):
        # surface???
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        #surface.blit(self.image,rect)

        # check out of rect
        if not(0 < self.x < window.get_rect().width):
            # reverse direction
            self.vx = self.vx * -1
        if not(0 < self.y < window.get_rect().height):
            # reverse direction
            self.vy = self.vy * -1
