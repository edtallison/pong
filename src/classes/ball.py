import pygame

class Ball:
    def __init__(self, width, height, colour):
        self.dim = 30
        self.size = (self.dim, self.dim)
        self.x_pos = (width/2) - (self.dim/2)
        self.y_pos = (height/2) - (self.dim/2)

        self.surf = pygame.Surface(self.size)
        self.surf.fill(colour)
    
    def move(self):
        self.x_pos += 10
        self.y_pos -= 10

    def update_pos(self, screen):
        screen.blit(self.surf, (self.x_pos,self.y_pos))