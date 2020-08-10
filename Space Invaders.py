# Based on TechwithTim tutorial: https://www.youtube.com/watch?v=Q-__8Xw9KTM&t=141s

import pygame 
import os
import time 
import random

# Game window
WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# Load Images
current_path = os.path.dirname(__file__) # Where your .py file is located
assets_path = os.path.join(current_path, 'assets') # The image folder path

RED_SPACE_SHIP = pygame.image.load(os.path.join(assets_path, "pixel_ship_red_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join(assets_path, "pixel_ship_green_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join(assets_path, "pixel_ship_blue_small.png"))

# Player Ship
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join(assets_path, "pixel_ship_yellow.png"))

# Lasers
RED_LASER = pygame.image.load(os.path.join(assets_path, "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join(assets_path, "pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join(assets_path, "pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join(assets_path, "pixel_laser_yellow.png"))

# Background
BG = pygame.image.load(os.path.join(assets_path, "background-black.png"))

def main():
    run = True
    FPS = 60
    clock = pygame.time.Clock()



    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            



if __name__ == "__main__":            
    main()



