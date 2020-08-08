import pygame 

#Initialize pygame
pygame.init()

#Creates pygame window (screen)
screen = pygame.display.set_mode((800,600))

#Title and Icon for window
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('space-invaders-icon.png')
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load("player.png")
playerX = 370
playerY = 480

def player():
    screen.blit(playerImg, (playerX, PlayerY))
    

#Game loop
#def main():
running = True
while running:
    #window background
    screen.fill((51, 51, 204))
    
    for event in pygame.event.get():
        #Quit event logic
        if event.type == pygame.QUIT:
            running = False


    player()
    pygame.display.update()

