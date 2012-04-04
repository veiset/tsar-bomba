import random
import time
import pygame, sys
import player as playerEntity
import world.floor as floor
import keypress
import physics


menuBG = pygame.Surface([250,720])
menuBG.set_alpha(178)
menuBG.fill((50,50,50))


fpsClock = pygame.time.Clock()

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Main')

keystate = keypress.Keypress()
player = playerEntity.Player('Vegard', (100,100), keystate)

f = floor.Floor((30,200,1000,10))

delta = (1/60.0)*1000
game = True
while game:
    for event in pygame.event.get():
        keystate.update(event)
    
    if keystate.state('QUIT'):
        pygame.quit()
        sys.exit()

    screen.fill((0,0,0))
    f.draw(screen)

    player.update(delta)
    player.draw(screen)

    pygame.display.update()
    fpsClock.tick(60)
    
