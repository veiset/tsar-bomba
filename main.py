import random
import time
import pygame, sys
import player as playerEntity
import world.floor as floor
import npc.bear as bearEntity
import npc.manne as manneEntity
import npc.moose as mooseEntity
import npc.police as policeEntity
import npc.dino as dinoEntity
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

npcs = []
npcs.append(bearEntity.Bear('Mofo', (400,100)))
npcs.append(manneEntity.Manne('F', (300,100)))
npcs.append(mooseEntity.Moose('MOO', (200,100)))
npcs.append(policeEntity.Police('lol', (500, 100)))
npcs.append(dinoEntity.Dino('hei', (600, 100)))

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

    for npc in npcs:    
        npc.update(delta)
        npc.draw(screen)

    pygame.display.update()
    fpsClock.tick(60)
    
