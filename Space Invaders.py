import pygame 
import os

#Initialize pygame
pygame.init()

#Creates pygame window (screen)
screen = pygame.display.set_mode((800,600))

#Title and Icon for window

current_path = os.path.dirname(__file__) # Where your .py file is located
image_path = os.path.join(current_path, 'Images') # The image folder path

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load(os.path.join(image_path, 'SpaceIcon.png'))
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load(os.path.join(image_path, 'SpaceshipPlayer.png'))
playerX = 370
playerY = 480
playerXDelta = 0
playerYDelta = 0

def player(x,y):
    screen.blit(playerImg, (x, y))

#Enemy
enemyImg = pygame.image.load(os.path.join(image_path, 'SpaceInvaderEnemy.png'))
enemyX = 370
enemyY = 480
enemyXDelta = 0
enemyYDelta = 0

def enemy(x,y):
    screen.blit(enemyImg, (x, y))


#Game loop
running = True
while running:
    #window background
    screen.fill((0, 0, 0))
    
    
    
    for event in pygame.event.get():
        #Quit event logic
        if event.type == pygame.QUIT:
            running = False
        
        #Keystroke events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerXDelta = -0.3
            if event.key == pygame.K_RIGHT:
                playerXDelta = 0.3
    
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerXDelta = 0
            
            
    playerX += playerXDelta
    #playerY -= playerYDelta

    if playerX <= 0:
        playerX = 0
    elif playerX >= 745:
        playerX = 745

    player(playerX, playerY)
    pygame.display.update()

