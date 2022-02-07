import pygame

class Paddle:
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

    def update_pos(self, screen):
        screen.blit(self.surf, (self.x_pos,self.y_pos))

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