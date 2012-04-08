import pygame
import physics
import random
import collision 

class Player():
    
    revModel = lambda x: [y[::-1] for y in x]

    modellist = {'RIGHT':[[0,             (255,128,0),   (242,217,193),  0],
                     [(255,128,0),    (242,217,193), (242,217,193),  0],
                     [0,              (255,0,0),     (0,255,0),      (0, 255,0)],
                     [0,              (255,0,0),     (255,0,0),      0]],


             'DOWN_RIGHT' :[[0, 0, 0, 0, 0],
                      [0, 0, 0, (255,128,0), (255,128,0)],
                      [0, (255,0,0), (255,0,0), (255,128,0), (242, 217, 193)],
                      [(255,0,0), (255,0,0), (255,0,0),0,0]]
            }
    modellist['LEFT'] = revModel(modellist['RIGHT'])
    modellist['DOWN_LEFT'] = revModel(modellist['DOWN_RIGHT'])

    def __init__(self, name, pos, keystate):
        self.name      = name
        self.x, self.y = pos
        self.dx = self.x
        self.dy = self.y
        self.model = self.modellist['RIGHT'] 
        self.onGround = False

        self.key = keystate
        self.size = 10

    def direction(self,x,y):
        direction = {'RIGHT': False, 'LEFT': False, 'UP': False, 'DOWN': False}
        if (self.x+x>self.x):
            direction['RIGHT'] = True
        if (self.x+x<self.x):
            direction['LEFT'] = True
        if (self.y+y<self.y):
            direction['UP'] = True
        if (self.y+y>self.y):
            direction['DOWN'] = True
        return direction

    def nextModel(self,x,y):
        d = self.direction(x,y)
        if (d['LEFT']):
            return self.modellist['LEFT']
        elif (d['RIGHT']):
            return self.modellist['RIGHT']
        return self.model

    def update(self, delta):

        self.dy = self.y
        self.dx = self.x

    
    def pushOffX(self, a, b):
        '''
        a -- boundedBox from self.model 
        b -- boundedBox of another entity
        '''
        if a.hitsLeftOf(b):
            self.x -= (a.right - b.left)
        elif a.hitsRightOf(b):
            self.x += (b.right - a.left)

    def pushOffY(self, a, b):
        '''
        a -- boundedBox from self.model 
        b -- boundedBox of another entity
        '''
        if a.hitsTopOf(b):
            self.y -= a.bottom - b.top
        elif a.hitsBottomOf(b):
            self.y += b.bottom - a.top


    def draw(self, screen):
        m = self.model
        
        for r, row in enumerate(m):
            for i, element in enumerate(row):
                if element:
                    pygame.draw.rect(screen, element, (int(round(self.x,0))+(self.size*i), int(round(self.y,0))+(self.size*r)-len(m)*self.size, self.size, self.size)) 
        
