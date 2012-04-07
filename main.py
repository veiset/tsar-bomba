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
player = playerEntity.Player('Vegard', (50,250), keystate)

npcs = []
npcs.append(bearEntity.Bear('Mofo', (400,100)))
npcs.append(manneEntity.Manne('F', (300,100)))
npcs.append(mooseEntity.Moose('MOO', (200,100)))
npcs.append(policeEntity.Police('lol', (500, 100)))
npcs.append(dinoEntity.Dino('hei', (600, 100)))


som.add('Tree01',(200,500))
som.add('Tree01',(100,500),'background')
som.add('Tree01',(400,500),'player')
som.add('Floor01',(0,520),'player')
som.add('Floor01',(0,520),'player')
som.add('Floor01',(200,520),'player')
som.add('Floor01',(400,520),'player')
som.add('Floor01',(230,320),'player')
som.add('IceTap01',(500,280),'player')

delta = (1/60.0)*1000
game = True
while game:
    for event in pygame.event.get():
        keystate.update(event)
    
    if keystate.state('QUIT'):
        pygame.quit()
        sys.exit()

    movex = 0
    movey = 0
    # Handle input
    if keystate.state('LEFT'):
        movex += -2.0
    if keystate.state('RIGHT'):
        movex += 2.0
    if keystate.state('DOWN'):
        ''' nothing currently '''
        #movey += 2.0
    if keystate.state('UP'):
        if player.onGround:
            movey += -5.5
    


    movey -= physics.gravity(player.y, player.dy, delta)

    bound = collision.calcBound(player.nextModel(movex,movey), (player.x+movex, player.y+movey), player.size)
    cols = []
    #t = time.time()
    #for el in som.player:
    #    r = collision.collision(bound, el['bbox'])
    #    cols.extend(r)
    #print time.time()-t

    static = collision.calcBound(*som.getStaticGrid((player.x, player.y), 4, 4))
    cols = collision.collision(bound, static)

    groundTiles = []
    cilingTiles = []
    leftTiles   = []
    rightTiles  = []
   
    player.onGround = False

    for col in cols:
        a, b = col
        if a.hitsLeftOf(b) and a.xOverlap(b) < a.yOverlap(b):
            leftTiles.append(b)
            movex = 0
        if a.hitsRightOf(b) and a.xOverlap(b) < a.yOverlap(b):
            rightTiles.append(b)
            movex = 0
        if a.hitsTopOf(b) and a.yOverlap(b) <= a.xOverlap(b):
            groundTiles.append(col)
            movey = 0
            player.onGround = True

        if a.hitsBottomOf(b) and a.yOverlap(b) <= a.xOverlap(b):
            cilingTiles.append(col)
            movey = 0


    for col in cilingTiles:
        a, b = col
        if (a.intersect(b)):
            cols.remove(col)

    if not player.onGround:
        for col in cols:
            a, b = col
            if a.intersect(b):
                if (a.hitsLeftOf(b) or a.hitsRightOf(b)):
                    ''' '''
    else:
        for col in groundTiles:
            a, b = col
            if (a.intersect(b)):
                if (a.hitsTopOf(b)):
                    try:
                        cols.remove(col)
                    except:
                        ''' tile was also a ciling '''

    for col in cols:
        a, b = col
        if a.intersect(b):
            if (a.hitsRightOf(b) or a.hitsLeftOf(b)):
                ''' '''

    if not cols:
        player.model = player.nextModel(movex,movey)


    player.update(delta)
    player.x += movex
    player.y += movey



    # Draw stuff
    screen.fill((0,0,0))
    som.draw(screen, som.background)
    som.draw(screen, som.player)
    player.draw(screen)
    som.draw(screen, som.front)

    pygame.display.update()
    fpsClock.tick(60)
    
