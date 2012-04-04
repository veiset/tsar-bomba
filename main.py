import random
import time
import pygame, sys
from pygame.locals import *
import player

menuBG = pygame.Surface([250,720])
menuBG.set_alpha(178)
menuBG.fill((50,50,50))


fpsClock = pygame.time.Clock()

pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Main')

pl = player.Player('Vegard', (100,100))
move = {'LEFT'  : False,
        'RIGHT' : False,
        'UP'    : False,
        'DOWN'  : False}


lastArrow = 'RIGHT' 

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_UP:
                move['UP'] = True
            elif event.key == K_DOWN:
                move['DOWN'] = True
            elif event.key == K_LEFT:
                move['LEFT'] = True
                lastArrow = 'LEFT' 
            elif event.key == K_RIGHT:
                move['RIGHT'] = True 
                lastArrow = 'RIGHT' 

        elif event.type == KEYUP:
            if event.key == K_UP:
                move['UP'] = False 
            elif event.key == K_DOWN:
                move['DOWN'] = False
            elif event.key == K_LEFT:
                move['LEFT'] = False
            elif event.key == K_RIGHT:
                move['RIGHT'] = False 

    screen.fill((0,0,0))
    
    if move['RIGHT']:
        if move['DOWN']:
            pl.x += 1
        else:
            pl.x += 2
    if move['LEFT']:
        if move['DOWN']:
            pl.x -= 1
        else:
            pl.x -= 2

    if move['DOWN']:
        if lastArrow == 'RIGHT':
            pl.animation = 'DOWN_RIGHT'
        else:
            pl.animation = 'DOWN_LEFT'

    elif move['RIGHT']:
        pl.animation = 'RIGHT'
    elif move['LEFT']:
        pl.animation = 'LEFT'

    pl.draw(screen)

    pygame.display.update()
    fpsClock.tick(60)
    
