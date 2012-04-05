import random
import time
import pygame, sys
from pygame.locals import *
import colset

fpsClock = pygame.time.Clock()

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Main')


game = True
rgb = [0, 0, 0]
multi = False
colors = []
c = 0
l = []
for x in colset.rgb:
    l.append(x)     
    c += 1
    if (c==16):
        c = 0
        colors.append(l)
        l = []

lastUsed = []

def outputModel():
    print '---- COPY & PASTE -----'
    mx = 0
    my = 0
    for x, row in enumerate(model):
        for y, el in enumerate(row):
            if el and y > my:
                my = y
            if el and x > mx:
                mx = x
    mx += 1
    my += 1

    print "model['MOTION'] = ["
    for y in range(my):
        print "[",
        for x in range(mx):
            print model[x][y],",",
        print "],"
    print "]"


colors.append(l)
pygame.mouse.set_visible(1)

currentCol = (255,0,0)
model = [[0 for _ in range(20)] for _ in range(20)]
while game:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == MOUSEBUTTONDOWN:
            mx, my = event.pos
            if mx < 200 and my<500:
                try:
                    currentCol = colors[my/12][mx/12]
                    lastUsed.append(currentCol)
                except:
                    print 'out of bound'
            elif mx < 200 and 520>my>500:
                try:
                    currentCol = lastUsed[::-1][mx/20]
                except:
                    print 'out of bound'
            elif mx < 30 and 600>my>570:
                model = [[0 for _ in range(20)] for _ in range(20)]
            elif mx>200:
                index = ((mx-200)/30, (my)/30)
                if event.button == 1:
                    model[index[0]][index[1]] = currentCol
                else:
                    model[index[0]][index[1]] = 0

        if event.type == KEYDOWN:
            outputModel()
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    screen.fill((0,0,0))

    for x in range(20):
        pygame.draw.line(screen, (100,100,100), (200+(30*x), 0), (200+(30*x),600))
        pygame.draw.line(screen, (100,100,100), (200, 30*x),  (800, 30*x))

    for x in range(255):
        pygame.draw.rect(screen, currentCol, (0,520,200,200))
    
    for x, row in enumerate(colors):
        for y, color in enumerate(row):
            pygame.draw.rect(screen, color, (y*12, x*12, 12, 12)) 

    for x, row in enumerate(model):
        for y, el in enumerate(row):
            if el:
                pygame.draw.rect(screen, el, (200+(30*x),30*y,30,30))

    for x, c in enumerate(lastUsed[::-1][0:10]):
        pygame.draw.rect(screen, c, ((x*20), 500, 20, 20))

    pygame.draw.rect(screen, (0,0,0), (0, 570, 30, 30))

    pygame.display.update()
    fpsClock.tick(60)
    

