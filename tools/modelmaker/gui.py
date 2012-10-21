import pygame
import colset 

class GUI():
    '''
    TODO: Fix scaling, remove magic constants
    '''

    def __init__(self, screen):
        self.screen = screen
        self.SWIDTH, self.SHEIGHT = screen.get_size()

        self.colorgrid = pygame.Surface((self.SWIDTH, self.SHEIGHT), pygame.SRCALPHA)
        self.lines = pygame.Surface((self.SWIDTH, self.SHEIGHT), pygame.SRCALPHA)
        self.frameTabs = pygame.Surface((self.SWIDTH, self.SHEIGHT), pygame.SRCALPHA)
        self.clearButton = pygame.Surface((self.SWIDTH, self.SHEIGHT), pygame.SRCALPHA)
        self.speedButton = pygame.Surface((self.SWIDTH, self.SHEIGHT), pygame.SRCALPHA)
        self.currentTab = pygame.Surface((self.SWIDTH, self.SHEIGHT), pygame.SRCALPHA)

        self.playButton = pygame.image.load("img/play.png").convert()

        # Nothing to currently draw on the following surfaces 
        self.frame = pygame.Surface((self.SWIDTH, self.SHEIGHT), pygame.SRCALPHA)
        self.colorHistory = pygame.Surface((self.SWIDTH, self.SHEIGHT), pygame.SRCALPHA)
        self.color = pygame.Surface((self.SWIDTH, self.SHEIGHT), pygame.SRCALPHA)

        self.drawCurrentTab(0)
        self.drawSpeedButton()
        self.drawLines()
        self.drawColorGrid()
        self.drawFrameTabs()
        self.drawClearButton()


    def drawSpeedButton(self):
        pygame.draw.rect(self.speedButton, (0,150,0), (800-(30*2),0,30,30))

    def drawClearButton(self):
        pygame.draw.rect(self.clearButton, (0,0,0), (0, 570, 30, 30))


    def drawFrameTabs(self):
        for x in range(20):
            pygame.draw.rect(self.frameTabs, (255-(x*10),)*3, (200+(30*x),0,30,30))
        
    def drawLines(self):
        for x in range(20):
            pygame.draw.line(self.lines, (100,100,100), (200+(30*x), 0), (200+(30*x),600))
            pygame.draw.line(self.lines, (100,100,100), (200, 30*x),  (800, 30*x))

    def drawColorGrid(self):
        for x, row in enumerate(colset.colorList()):
            for y, color in enumerate(row):
                pygame.draw.rect(self.colorgrid, color, (y*12, x*12, 12, 12)) 

    def drawFrame(self, grid):
        self.frame = pygame.Surface((self.SWIDTH, self.SHEIGHT), pygame.SRCALPHA)
        for x, row in enumerate(grid):
            for y, el in enumerate(row):
                if el:
                    pygame.draw.rect(self.frame, el, (200+(30*x),30*y,30,30))

    def drawColorHistory(self, history):
        self.colorHistory = pygame.Surface((self.SWIDTH, self.SHEIGHT), pygame.SRCALPHA)
        for x, c in enumerate(history[::-1][0:10]):
            pygame.draw.rect(self.colorHistory, c, ((x*20), 500, 20, 20))

    def drawCurrentTab(self, tab):
        self.currentTab = pygame.Surface((self.SWIDTH, self.SHEIGHT), pygame.SRCALPHA)
        pygame.draw.rect(self.currentTab, (242,150,150), (200+(30*tab),0,30,30))

    def drawColor(self, color):
        self.color = pygame.Surface((self.SWIDTH, self.SHEIGHT), pygame.SRCALPHA)
        pygame.draw.rect(self.color, color, (0,520,200,200))
        
    def blitLines(self): self.screen.blit(self.lines, (0,0))
    def blitColorGrid(self): self.screen.blit(self.colorgrid, (0,0))
    def blitFrameTabs(self): self.screen.blit(self.frameTabs, (0,0))
    def blitSpeedButton(self): self.screen.blit(self.speedButton, (0,0))
    def blitPlayButton(self): self.screen.blit(self.playButton, (800-30, 0))
    def blitClearButton(self): self.screen.blit(self.clearButton, (0,0))
    def blitFrame(self): self.screen.blit(self.frame, (0,0))
    def blitColorHistory(self): self.screen.blit(self.colorHistory, (0,0))
    def blitCurrentTab(self): self.screen.blit(self.currentTab, (0,0))
    def blitColor(self): self.screen.blit(self.color, (0,0))

    def areaColorGrid(self,mx,my): 
        return (mx < 200 and my < 500)

    def areaHistoryTab(self,mx,my):
        return (mx < 200 and 520>my>500)

    def areaClearBoardButton(self,mx,my):
        return (mx < 30 and 600>my>570)

    def areaModel(self,mx,my):
        return (mx>200 and my>30)

    def areaModelTab(self,mx,my):
        return (mx>200 and my<30)

    def areaPlayButton(self,mx,my):
        return (mx>200 and ((mx-200)/30 == 19) and my<30)

    def areaSpeedButton(self,mx,my):
        return (mx>200 and ((mx-200)/30 == 18) and my<30)
  
