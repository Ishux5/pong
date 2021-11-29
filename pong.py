import pygame
import random

WIDTH, HEIGHT = 1000, 700
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

FPS = 120
PLAYERWIDTH, PLAYERHEIGHT = 18, 120
BALL_WIDTH, BALL_HEIGHT = 14, 14
MID_BOUND_WIDTH, MID_BOUND_HEIGHT = 8, HEIGHT
PLAYER_VEL = 5


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_GRAY = (10, 10, 10)

font = pygame.font.init()
SCORE_FONT = pygame.font.SysFont("framd.ttf", 240)


def ballMovement(ball, ballVelX, ballVelY):
    ball.x += ballVelX
    ball.y += ballVelY


def playerMovement(keyPress, playerOne, playerTwo):
    if keyPress[pygame.K_w] and playerOne.y > 0:
        playerOne.y -= PLAYER_VEL
    if keyPress[pygame.K_s] and playerOne.y < HEIGHT - PLAYERHEIGHT:
        playerOne.y += PLAYER_VEL
    if keyPress[pygame.K_UP] and playerTwo.y > 0:
        playerTwo.y -= PLAYER_VEL
    if keyPress[pygame.K_DOWN] and playerTwo.y < HEIGHT - PLAYERHEIGHT:
        playerTwo.y += PLAYER_VEL


def playerCollisions(ball, playerOne, playerTwo, ballVelX):
    if ball.colliderect(playerOne):
        ballVelX = -1 * ballVelX


def drawWindow(playerOne, playerTwo, ball, p1Score, p1Width, p1Height, p2Score, p2Width, p2Height):
    WINDOW.fill(BLACK)
    WINDOW.blit(p1Score, (WIDTH / 4 - p1Width / 2, HEIGHT / 2 - p1Height / 2))
    WINDOW.blit(p2Score, (WIDTH / 4 * 3 - p2Width /
                2, HEIGHT / 2 - p2Height / 2))
    pygame.draw.rect(WINDOW, LIGHT_GRAY, pygame.Rect(
        WIDTH / 2 - MID_BOUND_WIDTH / 2, 0, MID_BOUND_WIDTH, MID_BOUND_HEIGHT))
    pygame.draw.rect(WINDOW, WHITE, playerOne)
    pygame.draw.rect(WINDOW, WHITE, playerTwo)
    pygame.draw.rect(WINDOW, WHITE, ball, border_radius=4)

    pygame.display.update()


def main():
    # scores:
    playerOneScore = 0
    playerTwoScore = 0

    playerOne = pygame.Rect(
        0, HEIGHT / 2 - PLAYERHEIGHT / 2, PLAYERWIDTH, PLAYERHEIGHT)

    playerTwo = pygame.Rect(WIDTH - PLAYERWIDTH, HEIGHT /
                            2 - PLAYERHEIGHT / 2, PLAYERWIDTH, PLAYERHEIGHT)

    ball = pygame.Rect(WIDTH / 2 - BALL_WIDTH / 2, HEIGHT /
                       2 - BALL_HEIGHT / 2, BALL_WIDTH, BALL_HEIGHT)

    clock = pygame.time.Clock()
    run = True
    firstMove = True
    while run:
        keyPress = pygame.key.get_pressed()

        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        renderP1Score = SCORE_FONT.render(
            str(playerOneScore), True, LIGHT_GRAY)
        p1ScoreWidth, p1ScoreHeight = renderP1Score.get_width(), renderP1Score.get_height()
        renderP2Score = SCORE_FONT.render(
            str(playerTwoScore), True, LIGHT_GRAY)
        p2ScoreWidth, p2ScoreHeight = renderP2Score.get_width(), renderP2Score.get_height()

        if firstMove:
            ballVelX = 3
            ballVelY = 0

            xDirection = random.randint(0, 1)
            ballVelY = round(random.randint(-1 * ballVelX, ballVelX))
            if xDirection == 0:
                ballVelX = -1 * ballVelX

            firstMove = False

        if ball.y <= 0:
            ballVelY = ballVelY * -1
        elif ball.y >= HEIGHT - BALL_HEIGHT:
            ballVelY = ballVelY * -1

        if ball.x < 0:
            playerTwoScore += 1
            ball.x = WIDTH / 2 - BALL_WIDTH / 2
            ball.y = HEIGHT / 2 - BALL_HEIGHT / 2
            firstMove = True
        if ball.x > WIDTH:
            playerOneScore += 1
            ball.x = WIDTH / 2 - BALL_WIDTH / 2
            ball.y = HEIGHT / 2 - BALL_HEIGHT / 2
            firstMove = True

        if ball.colliderect(playerOne):
            ballVelX = -1 * ballVelX
            if keyPress[pygame.K_w] and ballVelY <= 0 and ballVelY < abs(ballVelX):
                ballVelY -= 1
            elif keyPress[pygame.K_s] and ballVelY >= 0 and ballVelY < abs(ballVelX):
                ballVelY += 1
        if ball.colliderect(playerTwo):
            ballVelX = -1 * ballVelX
            if keyPress[pygame.K_UP] and ballVelY <= 0 and ballVelY < abs(ballVelX):
                ballVelY -= 1
            elif keyPress[pygame.K_DOWN] and ballVelY >= 0 and ballVelY < abs(ballVelX):
                ballVelY += 1

        playerMovement(keyPress, playerOne, playerTwo)
        playerCollisions(ball, playerOne, playerTwo, ballVelX)
        ballMovement(ball, ballVelX, ballVelY)
        drawWindow(playerOne, playerTwo, ball, renderP1Score, p1ScoreWidth,
                   p1ScoreHeight, renderP2Score, p2ScoreWidth, p2ScoreHeight)


if __name__ == "__main__":
    main()
