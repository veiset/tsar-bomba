import pygame
from pygame.locals import *
import random
import time
import sys
import colset
import output
from gui import GUI
from model import PixelModel

fpsClock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('tsar-bomba - Model Maker')
pygame.mouse.set_visible(1)


running = True
playAnim = False
speed = 0
colors = colset.colorList()
currentColor = (255,0,0)
colorHistory = []
frameIndex = 0

gui = GUI(screen) # all static parts of the GUI is drawn
gui.drawColor(currentColor)

speedTicks = [1,3,6,10,30]
model = PixelModel(20,20,20)

f = file("models/fire.json","r")
model = output.jsonToModel(f.read())
f.close()
gui.drawFrame(model.frame(frameIndex).grid)

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == MOUSEBUTTONDOWN:
            mx, my = event.pos
            mxGrid = (mx-200)/30
            myGrid = my/30
            currentFrame = model.frame(frameIndex) 

            if gui.areaColorGrid(mx,my):
                try:
                    currentColor = colors[my/12][mx/12]
                    colorHistory.append(currentColor)
                    gui.drawColorHistory(colorHistory)
                    gui.drawColor(currentColor)
                except: print 'out of bound'

            elif gui.areaHistoryTab(mx,my):
                try:
                    currentColor = colorHistory[::-1][mx/20]
                    gui.drawColor(currentColor)
                except: print 'out of bound'

            elif gui.areaClearBoardButton(mx,my): 
                currentFrame.clear()
                gui.drawFrame(currentFrame.grid)

            elif gui.areaModel(mx,my):
                index = (mxGrid, myGrid)
                if event.button == 1: 
                    currentFrame.setPixel(mxGrid, myGrid, currentColor)
                else: 
                    currentFrame.delPixel(mxGrid, myGrid)
                gui.drawFrame(currentFrame.grid)

            elif gui.areaPlayButton(mx,my):
                playAnim = not playAnim
                if playAnim: 
                    frameIndex = 0
                    print("Animation: Playing")
                else:
                    print("Animation: Stopped")

            elif gui.areaSpeedButton(mx,my):
                if (speed+1) == len(speedTicks): speed = 0
                else: speed += 1
                print("Animation speed:", speed)

            elif gui.areaModelTab(mx,my):
                if (frameIndex == mxGrid) and 19>mxGrid>0:
                    model.copyPreviousFrame(frameIndex)
                    print("Copying previous frame")

                print("Model frame tab:", mxGrid)
                frameIndex = mxGrid
                gui.drawFrame(model.frame(frameIndex).grid)
                gui.drawCurrentTab(frameIndex)

        if event.type == KEYDOWN:
            print output.modelToJson(model)
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    if playAnim:
        if model.frame(frameIndex+1).isEmpty():
            frameIndex = 0
        else:
            frameIndex += 1
        gui.drawFrame(model.frame(frameIndex).grid)
        gui.drawCurrentTab(frameIndex)

    screen.fill((0,0,0))

    gui.blitLines()
    gui.blitColorGrid()
    gui.blitFrameTabs()
    gui.blitFrame()
    gui.blitColorHistory()
    gui.blitPlayButton()
    gui.blitCurrentTab()
    gui.blitSpeedButton() 
    gui.blitColor()
    gui.blitClearButton()

    pygame.display.update()

    if playAnim:
        fpsClock.tick(speedTicks[speed])
    else:
        fpsClock.tick(60)
