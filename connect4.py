# git add <file name> <file 2>
# git commit -m "comment"
# git push origin master

import pygame
import sys
import random
import math

pygame.init()
gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Connect 4')

grey = (100,100,100)
blue = (0,150,255)
green = (50,255,50)
black = (0,0,0)
red = (255,0,0)
yellow = (255,255,0)
white = (255,255,255)
crashed = False
clock = pygame.time.Clock()
game_board = pygame.image.load('connect-four-gameboard.png')
moveCoin = 4


def text_objects(text, font, color):
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()

def message_display(text, text_x, text_y, text_size, color):
        largeText = pygame.font.Font('freesansbold.ttf',text_size)
        TextSurf, TextRect = text_objects(text, largeText, color)
        TextRect.center = (text_x, text_y)
        gameDisplay.blit(TextSurf, TextRect)

# One iter of this while loop = basically 1 frame
while not crashed:

    # On a single frame, this for goes through each event made because multiple events could have been made
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and moveCoin != 1:
                moveCoin += -1
                print("moveCoin has changed by 1")
            if event.key == pygame.K_RIGHT and moveCoin != 7:
                moveCoin += 1
                print("moveCoin has changed by -1")


        
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_r and (player_1_wins == True or player_2_wins == True or tieGame == True):
        #         p1 = True
        #         p2 = False
        #         player_1_wins = False
        #         player_2_wins = False
        #         tieGame = False
        #         allQuadrants = [0,0,0,0,0,0,0,0,0]
        

    # If it should run every frame it should be under this

    # All drawing should be under this
    gameDisplay.fill(grey)
    gameDisplay.blit(pygame.transform.scale(game_board,(500,500)), (150,120))
    pygame.draw.circle(gameDisplay, red, ((116+(moveCoin*71)),50), 30)
    # print(moveCoin)



    pygame.display.update()
    clock.tick(60)