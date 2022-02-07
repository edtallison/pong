import pygame
from classes.object import Object

class Paddle(Object):
    def __init__(self, x_pos, screen_height, colour):
        self.height = 200
        self.x_pos = x_pos
        self.screen_height = screen_height
        self.y_pos = (self.screen_height / 2) - (self.height / 2)
        
        # Create the rectangle to be drawn on the screen
        self.surf = pygame.Surface((50, self.height))
        self.surf.fill(colour)

    def move(self, up, down):
        if self.y_pos > 0:
            self.y_pos -= up * 10
            
        if self.y_pos < (self.screen_height - self.height):
            self.y_pos += down * 10