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
        self.y_pos = 300
        # Create the rectangle to be drawn on the screen
        self.surf = pygame.Surface((50, 200))
        self.surf.fill(white)

    def move(self, up, down):
        self.y_pos -= up * 10
        self.y_pos += down * 10

    def update_pos(self):
        screen.blit(self.surf, (self.x_pos,self.y_pos))

pLeft = player(100)
pRight = player(1050)

# Add clock/time to smooth out framerate
clock = pygame.time.Clock()

# Game loop
while 1:
    # Lets the user close the game
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
            sys.exit()
    # Get key presses from user
    keys = pygame.key.get_pressed()

    pLeft.move(keys[pygame.K_w], keys[pygame.K_s])
    pRight.move(keys[pygame.K_UP], keys[pygame.K_DOWN])

    # Update screen with positions of players
    screen.fill(black)
    pLeft.update_pos()
    pRight.update_pos()
    pygame.display.flip()

    clock.tick(30)