import random
import time
import pygame, sys
import player as playerEntity
import keypress
import physics
import objectmanager
import levelmanager
import collision

fpsClock = pygame.time.Clock()
pygame.init()

SWIDTH, SHEIGHT = 800, 600

screen = pygame.display.set_mode((SWIDTH, SHEIGHT)) #, pygame.DOUBLEBUF | pygame.HWSURFACE) 
pygame.display.set_caption('Tsar Bomba')

keystate = keypress.Keypress()
player = playerEntity.Player('Vegard', (50,250), keystate)

som = objectmanager.StaticObjectManager(screen)
level = levelmanager.LevelManager(som)
level.load('01')

delta = (1/60.0)*1000
game = True
fpsc = 0
t = time.time()
tile = [0,0]

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
    elif keystate.state('RIGHT'):
        movex += 2.0
    if keystate.state('DOWN'):
        ''' nothing currently '''
        #movey += 2.0
    if keystate.state('UP'):
        if player.onGround:
            movey += -5.5
    
    movey -= physics.gravity(player.y, player.dy, delta)

    bound = collision.calcBound(player.nextModel(movex,movey), (player.x+movex, player.y+movey), player.size)
    static = collision.calcBound(*som.getStaticGrid((player.x, player.y), 4, 4))

    cols = collision.collision(bound, static)
    collision.moveable(player, cols, movex, movey, delta)

    # Draw stuff
    screen.fill((0,0,0))
    som.blitBackground()
    som.blitGround()
    player.draw(screen)
    som.blitForeground()

    fpsClock.tick(60)
    pygame.display.flip()

    playerSizeX, playerSizeY = player.bbox()

    if player.x > SWIDTH-(playerSizeX/2): # TODO figure out this magic constant
        player.x = -playerSizeX/2
        print("Changed level x+1")
    if player.x < -playerSizeX/2:
        player.x = SWIDTH-(playerSizeX/2) 
        print("Changed level x-1")
    if player.y > SHEIGHT+(playerSizeY/2):
        player.dy -= player.y 
        player.y = 0
        print("Changed level y-1")
    

    # FPS
    fpsc += 1
    if fpsc == 60:
        fpsc = 0
        pygame.display.set_caption("Tsar Bomba - FPS: " +  str(int(60.0/(time.time()-t))))
        print(int(60.0/(time.time()-t)))
        t = time.time()
