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
model = [[0 for _ in range(10)] for _ in range(10)]
while game:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == MOUSEBUTTONDOWN:
            mx, my = event.pos
            if mx < 200:
                try:
                    currentCol = colors[my/12][mx/12]
                except:
                    print 'out of bound'
            else:
                index = ((mx-200)/60, (my)/60)
                if event.button == 1:
                    model[index[0]][index[1]] = currentCol
                else:
                    model[index[0]][index[1]] = 0

        if event.type == KEYDOWN:
            outputModel()

    screen.fill((0,0,0))

    for x in range(10):
        pygame.draw.line(screen, (100,100,100), (200+(60*x), 0), (200+(60*x),600))
        pygame.draw.line(screen, (100,100,100), (200, 60*x),  (800, 60*x))

    for x in range(255):
        pygame.draw.rect(screen, currentCol, (0,520,200,200))
    
    for x, row in enumerate(colors):
        for y, color in enumerate(row):
            pygame.draw.rect(screen, color, (y*12, x*12, 12, 12)) 

    for x, row in enumerate(model):
        for y, el in enumerate(row):
            if el:
                pygame.draw.rect(screen, el, (200+(60*x),60*y,60,60))


    pygame.display.update()
    fpsClock.tick(60)
    

