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
column1 = [0,0,0,0,0,0]
column2 = [0,0,0,0,0,0]
column3 = [0,0,0,0,0,0]
column4 = [0,0,0,0,0,0]
column5 = [0,0,0,0,0,0]
column6 = [0,0,0,0,0,0]
column7 = [0,0,0,0,0,0]
allColumn = [column1,column2,column3,column4,column5,column6,column7]
player = 1
column_has_change = False
player1wins = False
player2wins = False


def isFull(column):
    for elem in column:
        if elem == 0:
            return False
    return True

def check_if_player_wins(player, allColumn):
    if player == 1:
        score = 4
    else:
        score = 20
    for i in range (0,6):
        for j in range (0,2):
            if (allColumn[i] [0+j]) + (allColumn[i] [1+j]) + (allColumn[i] [2+j]) + (allColumn[i] [3+j]) == score:
                return True
    for i in range (0,5):
        for j in range (0,3):
            if (allColumn[0+j] [i]) + (allColumn[1+j] [i]) + (allColumn[2+j] [i]) + (allColumn[3+j] [i]) == score:
                return True
    for i in range (0,4):
        for j in range (0,3):
            if (allColumn[i] [j]) + (allColumn[i+1] [j+1]) + (allColumn[i+2] [j+2]) + (allColumn[i+3] [j+3]) == score:
                return True
    for i in range (6,2,-1):
        for j in range (0,3):
            if (allColumn[i] [j]) + (allColumn[i-1] [j+1]) + (allColumn[i-2] [j+2]) + (allColumn[i-3] [j+3]) == score:
                return True
    return False


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
            if event.key == pygame.K_RIGHT and moveCoin != 7:
                moveCoin += 1
            if event.key == pygame.K_r and (player1wins or player2wins) == True:
                column1 = [0,0,0,0,0,0]
                column2 = [0,0,0,0,0,0]
                column3 = [0,0,0,0,0,0]
                column4 = [0,0,0,0,0,0]
                column5 = [0,0,0,0,0,0]
                column6 = [0,0,0,0,0,0]
                column7 = [0,0,0,0,0,0]
                player1wins = False
                player2wins = False
                player = 1
                allColumn = [column1,column2,column3,column4,column5,column6,column7]
                
            if event.key == pygame.K_DOWN:
                if not isFull(allColumn[moveCoin - 1]):
                    column_has_change = False
                    for i, elem in enumerate(allColumn[moveCoin - 1]):
                        if elem == 0 and not column_has_change:
                            column_has_change = True
                            if player == 1:
                                allColumn[moveCoin - 1] [i] = 1
                                if check_if_player_wins(player, allColumn):
                                    player1wins = True
                                player = 2
                            else:
                                allColumn[moveCoin - 1] [i]= 5
                                if check_if_player_wins(player, allColumn):
                                    player2wins = True
                                player = 1
                            

    # If it should run every frame it should be under this

    # All drawing should be under this
    gameDisplay.fill(grey)
    gameDisplay.blit(pygame.transform.scale(game_board,(500,500)), (150,120))

    if player == 1:
        pygame.draw.circle(gameDisplay, red, ((116+(moveCoin*71)),50), 30)
    elif player == 2:
        pygame.draw.circle(gameDisplay, yellow, ((116+(moveCoin*71)),50), 30)

    j = 0
    for col in allColumn:
        i = 0
        for elem in col:
            if elem == 1:
                pygame.draw.circle(gameDisplay, red, ((185+(j*71)),(515-(i*71))), 30)
            elif elem == 5:
                pygame.draw.circle(gameDisplay, yellow, ((185+(j*71)),(515-(i*71))), 30)
            i += 1
        j += 1

    if player1wins:
        gameDisplay.fill(grey)
        message_display('player 1 wins', 400, 200, 115, red)
    if player2wins:
        gameDisplay.fill(grey)
        message_display('player 2 wins', 400, 200, 115, yellow)


    pygame.display.update()
    clock.tick(60)