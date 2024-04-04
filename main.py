# module Imports
import pygame

# Module Initialization
pygame.init()

# Game Assets and Objects

# Game Utility function

# Game Settings and Variables
SCREENWIDTH = 1260
SCREENHEIGHT = 960

# Colors``

# Pygame Dispaly Initialization
GAMESCREEN  = pygame.display.set_mode([SCREENWIDTH, SCREENHEIGHT])
pygame.display.set_caption("Battle Ship")
# Loading Game Variables

# Loading Game Sounds

# Initialize Players

# Main  Game Loop
RUNGAME = True
while RUNGAME:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNGAME  = False
    pygame.display.update()

pygame.quit()


