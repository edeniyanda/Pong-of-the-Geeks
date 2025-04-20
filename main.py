import sys
import pygame
import random

# Initilize Pygame
pygame.init()

# Set Clock for Game
clock = pygame.time.Clock() 

# Game Variables
GAME_NAME = "Pong of the Geeks"
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT) = (1200, 700)
BACKGROUND_COLOUR = pygame.Color("grey12")
LIGHT_GREY = (200,200,200)
MATRIX_GREEN = (0,255, 0)
NEON_CYAN = (0,255,255)
ELECTRIC_BLUE = (0, 191, 255)
LINE_MARGIN = 40


# Setting up main window and Caption
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption(GAME_NAME)


# Ball cordinates and property in space
ball = pygame.Rect(SCREEN_WIDTH//2-10, SCREEN_HEIGHT//2-10, 20, 20)
ball_xspeed  = random.choice((-7, 7))
ball_yspeed  = random.choice((-7, 7))

def teleportball():
    global ball_xspeed, ball_yspeed
    ball.center = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
    ball_xspeed *= random.choice((1,-1))
    ball_yspeed *= random.choice((1,-1))

def ballPropertiesAnimation():
    global ball_xspeed, ball_yspeed
    ball.x += ball_xspeed
    ball.y += ball_yspeed

    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        ball_yspeed *= -1
    if ball.left <= 0 or ball.right >= SCREEN_WIDTH:
        teleportball()

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_xspeed *= -1

# Player Geometry and Properties
player = pygame.Rect(SCREEN_WIDTH-15, SCREEN_HEIGHT//2 - 55, 10, 140)
player_speed = 0
def playerBatRestriction():
    global player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= SCREEN_HEIGHT:
        player.bottom = SCREEN_HEIGHT
# opponent cordinates and Properties
opponent = pygame.Rect(5, SCREEN_HEIGHT//2 - 55, 10, 140)
opponent_speed = 15
def opponentBatRestriction():
    global opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= SCREEN_HEIGHT:
        opponent.bottom = SCREEN_HEIGHT



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed +=7
            if event.key == pygame.K_UP:
                player_speed -=7

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed = 0
            if event.key == pygame.K_UP:
                player_speed = 0

    # Ball Animation 
    ballPropertiesAnimation()


    # Move player with specific speed
    player.y += player_speed

    # Player's Bat Restrition
    playerBatRestriction()

    # Player's Bat Restrition
    opponentBatRestriction()

    # Opponent movement
    if opponent.top < ball.y:
        opponent.top += opponent_speed 
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed 

    # Visuals
    screen.fill(BACKGROUND_COLOUR)
    pygame.draw.rect(screen, MATRIX_GREEN, player) 
    pygame.draw.rect(screen, MATRIX_GREEN, opponent)
    pygame.draw.ellipse(screen, MATRIX_GREEN, ball) 
    pygame.draw.aaline(screen, LIGHT_GREY, (SCREEN_WIDTH/2, 0), (SCREEN_WIDTH/2, SCREEN_HEIGHT))

    # update window
    pygame.display.flip()
    clock.tick(70)
