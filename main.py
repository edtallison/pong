import sys, pygame
pygame.init()

size = width, height = 1200, 800
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong!")

black = (0,0,0)
white = (255,255,255)

class paddle:
    def __init__(self, x_pos):
        self.height = 200
        self.x_pos = x_pos
        self.y_pos = (height / 2) - (self.height / 2)
        # Create the rectangle to be drawn on the screen
        
        self.surf = pygame.Surface((50, self.height))
        self.surf.fill(white)

    def move(self, up, down):
        if self.y_pos > 0:
            self.y_pos -= up * 10
            
        if self.y_pos < (height - self.height):
            self.y_pos += down * 10

    def update_pos(self):
        screen.blit(self.surf, (self.x_pos,self.y_pos))

class ball:
    def __init__(self):
        self.dim = 30
        self.size = (self.dim, self.dim)
        self.x_pos = (width/2) - (self.dim/2)
        self.y_pos = (height/2) - (self.dim/2)

        self.surf = pygame.Surface(self.size)
        self.surf.fill(white)

    def update_pos(self):
        screen.blit(self.surf, (self.x_pos,self.y_pos))

pLeft = paddle(100)
pRight = paddle(width - 150)
ball = ball()

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

    # Update screen with positions of paddles
    screen.fill(black)
    pLeft.update_pos()
    pRight.update_pos()
    ball.update_pos()
    pygame.display.flip()

    clock.tick(30)