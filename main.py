from re import L
import sys, pygame
pygame.init()

size = width, height = 1200, 800
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong!")

black = (0,0,0)
white = (255,255,255)

class player:
    def __init__(self, x_pos):
        self.x_pos = x_pos
        self.y_pos = 400
        self.surf = pygame.Surface((50, 200))
        self.surf.fill(white)

    def update_pos(self):
        screen.blit(self.surf, (self.x_pos,self.y_pos))

pLeft = player(100)
pRight = player(1050)

# Game loop
while 1:
    
    # Lets the user close the game
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()

    # Update screen with positions of players
    screen.fill(black)

    pLeft.update_pos()
    pRight.update_pos()

    pygame.display.flip()