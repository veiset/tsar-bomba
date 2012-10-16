import random
import time
import pygame, sys
from pygame.locals import *
import colset

fpsClock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Main')

playButton = pygame.image.load("img/play.png").convert()

game = True
activeTab = 0
# Generating colorset
colors = []
l = []
for i, x in enumerate(colset.rgb):
    l.append(x)     
    if ((i+1)%16==0): # display 16 colors per row
        colors.append(l)
        l = []
colors.append(l)

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

    print "    <ENTITY>"
    print "        <NAME>EditMe</NAME>"
    print "        <MODEL>"
    print "[",
    for y in range(my):
        print "[",
        for x in range(mx):
            print model[x][y],",",
        print "],"
    print "]"
    print "        </MODEL>"
    print "    </ENTITY>"

def gridEmpty(model):
    for row in model:
        for col in row:
            if col!=0: return False
    return True

def areaColorGrid(mx,my): 
    return (mx < 200 and my < 500)

def areaHistoryTab(mx,my):
    print (mx, my)
    return (mx < 200 and 520>my>500)

def areaClearBoardButton(mx,my):
    return (mx < 30 and 600>my>570)

def areaModel(mx,my):
    return (mx>200 and my>30)

def areaModelTab(mx,my):
    return (mx>200 and my<30)

def areaPlayButton(mx,my):
    return (mx>200 and ((mx-200)/30 == 19) and my<30)

def areaSpeedButton(mx,my):
    return (mx>200 and ((mx-200)/30 == 18) and my<30)

pygame.mouse.set_visible(1)

currentCol = (255,0,0)
def emptyModel():
    return [[0 for _ in range(20)] for _ in range(20)]

modelGrid = [emptyModel() for _ in range(20)]
model = modelGrid[0]
playAnim = False
speed = 0
speedTicks = [1,3,6,10,30]
while game:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == MOUSEBUTTONDOWN:
            mx, my = event.pos
            mxGrid = (mx-200)/30
            myGrid = my/30

            # Change color
            if areaColorGrid(mx,my):
                try:
                    currentCol = colors[my/12][mx/12]
                    lastUsed.append(currentCol)
                except:
                    print 'out of bound'
            elif areaHistoryTab(mx,my):
                try:
                    currentCol = lastUsed[::-1][mx/20]
                except:
                    print 'out of bound'
            elif areaClearBoardButton(mx,my):
                modelGrid[activeTab] = emptyModel()
                model = modelGrid[activeTab]
            elif areaModel(mx,my):
                index = (mxGrid, myGrid)
                if event.button == 1:
                    model[index[0]][index[1]] = currentCol
                else:
                    model[index[0]][index[1]] = 0
            elif areaPlayButton(mx,my):
                playAnim = not playAnim
                if playAnim:
                    activeTab = 0
            elif areaSpeedButton(mx,my):
                if (speed+1) == len(speedTicks): speed = 0
                else: speed += 1
                print("speed =", speed)
            elif areaModelTab(mx,my):
                # Copy model from prev grid
                if (activeTab == mxGrid) and 19>mxGrid>0:
                    # make a copy
                    copyTab = modelGrid[activeTab-1]
                    copy = []
                    for row in copyTab:
                        copy.append(list(row))
                    modelGrid[activeTab] = copy

                print("tab=", mxGrid)
                activeTab = mxGrid
                model = modelGrid[mxGrid]

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

    # Model tabs
    for x in range(20):
        pygame.draw.rect(screen, (255-(x*10),)*3, (200+(30*x),0,30,30))
    screen.blit(playButton, (800-30, 0))
    # Highlighted tab
    pygame.draw.rect(screen, (242,150,150), (200+(30*activeTab),0,30,30))
    # Speed Button 
    pygame.draw.rect(screen, (0,150,0), (800-(30*2),0,30,30))
    

    pygame.display.update()

    if playAnim:
        if gridEmpty(modelGrid[activeTab+1]):
            activeTab = 0
        else:
            activeTab += 1
        model = modelGrid[activeTab]
        fpsClock.tick(speedTicks[speed])
    else:
        fpsClock.tick(60)
