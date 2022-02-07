import pygame
from classes.object import Object

class Ball(Object):
    def __init__(self, screen_width, screen_height, colour):
        self.dim = 30
        self.size = (self.dim, self.dim)

        self.s_w = screen_width
        self.s_h = screen_height 
        self.x_pos = (self.s_w/2) - (self.dim/2)
        self.y_pos = (self.s_h/2) - (self.dim/2)

        self.surf = pygame.Surface(self.size)
        self.surf.fill(colour)

        self.vertical = 1
        self.horizontal = 1
    
    def move(self):

        if (self.y_pos < 0) or (self.y_pos > (self.s_h - self.dim)):
            self.vertical *= -1
        if (self.x_pos > (self.s_w - self.dim)) or (self.x_pos < 0):
            self.horizontal *= -1

        self.x_pos += self.horizontal * 10
        self.y_pos -= self.vertical * 10