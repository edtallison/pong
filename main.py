from re import L
import sys, pygame
pygame.init()

size = width, height = 1200, 800
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong!")

class player:
    def __init__(self, x_pos):
        self.x_pos = x_pos

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()