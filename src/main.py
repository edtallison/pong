import sys, pygame
sys.dont_write_bytecode = True
from classes.paddle import Paddle
from classes.ball import Ball
pygame.init()

def main():

    size = width, height = 1200, 800
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Pong!")

    black = (0,0,0)
    white = (255,255,255)

    pLeft = Paddle(100, height, white)
    pRight = Paddle(width - 150, height, white)
    ball = Ball(width, height, white)

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
        ball.move()

        # Update screen with positions of paddles
        screen.fill(black)
        pLeft.update_pos(screen)
        pRight.update_pos(screen)
        ball.update_pos(screen)
        pygame.display.flip()

        clock.tick(30)

if __name__ == "__main__":
    main()