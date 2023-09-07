import pygame 
from pygame.locals import *

# Game Variables
GAME_NAME = "Pong of the Geeks"
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = (600, 500)
BACKGROUND_COLOUR = (12,0,0)
WHITE_COLOR = (255,255,255)
LINE_MARGIN = 40


# Initialize Pygame
pygame.init()

gameclock = pygame.time.Clock()
fps = 60

# Game variable 
ai_score = 0
player_score = 0
font = pygame.font.SysFont("San Serif", 30)
ai = "E.R.I."
# Set Game Properties
game_screen = pygame.display.set_mode((SCREEN_SIZE)) # Set Screen Size
pygame.display.set_caption(GAME_NAME) #Set Game 

class bat:
    def __init__(self, x, y, bat_speed:int):
        self.x = x 
        self.y =  y
        self.rect = Rect(self.x, self.y, 10, 100)
        self.speed = bat_speed
        
    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_UP] and self.rect.top > LINE_MARGIN:
            self.rect.move_ip(0, -1 * self.speed)
        if key[pygame.K_DOWN] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.move_ip(0, self.speed)
    def draw(self):
        pygame.draw.rect(game_screen, WHITE_COLOR, self.rect)       
        

def draw_on_game_screen():
    game_screen.fill(BACKGROUND_COLOUR)
    pygame.draw.line(game_screen, WHITE_COLOR, (0, LINE_MARGIN), (SCREEN_WIDTH, LINE_MARGIN))

def draw_text_on_screen(text:str, font, text_colour, x, y):
    img = font.render(text, True, text_colour)
    game_screen.blit(img, (x,y))
    

# Bats
player_bat = bat(SCREEN_WIDTH - 20, SCREEN_HEIGHT // 2, 30) # Player Bat
ai_bat = bat(10, SCREEN_HEIGHT // 2, 30) # AI Bat


game_runing = True
# Game loop
while game_runing:
    gameclock.tick(fps)

    draw_on_game_screen()
    draw_text_on_screen(f"{ai}: {ai_score}", font, WHITE_COLOR, 10, 20)
    draw_text_on_screen(f"You: {player_score}", font, WHITE_COLOR, SCREEN_WIDTH - 100, 20)
    
    # Draw Bats
    player_bat.draw()
    ai_bat.draw()
    
    # Move Player's Bat
    player_bat.move()
    # Checking for all event in the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_runing= False 
            
    # Update Screen   
    pygame.display.update()        
pygame.quit()