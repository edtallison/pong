import pygame
from classes.object import Object

class Ball(Object):
    def __init__(self, screen_width, screen_height, colour):
        self.dim = 25
        self.size = (self.dim, self.dim)

        self.s_w = screen_width
        self.s_h = screen_height 
        self.x_pos = (self.s_w/2) - (self.dim/2)
        self.y_pos = (self.s_h/2) - (self.dim/2)

        self.surf = pygame.Surface(self.size)
        self.surf.fill(colour)

        self.vertical = 1
        self.horizontal = 1
    
    def check_collison(self, p1, p2):
        # Checks for bouncing on ceiling or floor
        if (self.y_pos < 0) or (self.y_pos > (self.s_h - self.dim)):
            self.vertical *= -1
        
        # Get important points from the 2 paddles
        x1, y1a, y1b = p1.x_pos + p1.width, p1.y_pos, p1.y_pos + p1.height
        x2, y2a, y2b = p2.x_pos, p2.y_pos, p2.y_pos + p2.height

        if ((self.x_pos < x1) and ((self.y_pos > y1a) and ((self.y_pos + self.dim) < y1b)))     or     (((self.x_pos + self.dim) > x2) and (self.y_pos > y2a) and ((self.y_pos + self.dim) < y2b)):
            self.horizontal *= -1
    
    def move(self):
        self.x_pos += self.horizontal * 10
        self.y_pos -= self.vertical * 10