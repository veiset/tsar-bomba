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
import objectmanager
import collision

som = objectmanager.StaticObjectManager()
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


som.add('Tree01',(200,500))
som.add('Tree01',(100,500),'background')
som.add('Tree01',(400,500),'player')
som.add('IceTap01',(500,280))
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

    som.draw(screen, som.background)
    f.draw(screen)


    direction = player.direction()
    col = collision.overlap(player.hitbox(),som.hitbox(som.player[0]))
    if col:
        if direction['LEFT'] and not player.blocked['LEFT']:
            player.blocked['LEFT'] = True

        if direction['RIGHT'] and not player.blocked['RIGHT']:
            player.blocked['RIGHT'] = True

        if direction['UP'] and not player.blocked['UP']:
            player.blocked['UP'] = True
            #player.y = player.dy

        if direction['DOWN'] and not player.blocked['DOWN']:
            player.blocked['DOWN'] = True
            #player.y = player.dy
    else:
        player.blocked = {'LEFT' : False,
                        'RIGHT': False,
                        'DOWN' : False,
                        'UP'   : False}

    player.update(delta)

    som.draw(screen, som.player)
    player.draw(screen)


    #for npc in npcs:    
    #    npc.update(delta)
    #    npc.draw(screen)

    som.draw(screen, som.front)

    pygame.display.update()
    fpsClock.tick(60)
    
