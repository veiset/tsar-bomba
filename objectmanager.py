from xml.etree import ElementTree as ET
import pygame
import collision 

class StaticObjectManager():

    def __init__(self):
        self.grid = {}

        xml = open('data/static/entities.xml','r')
        root = ET.XML(xml.read())
        xml.close()

        self.entities = {}

        self.background = []
        self.player = []
        self.front = []
        self.size = 10
        
        self.entityDict = {'background': self.background,
                           'player'    : self.player,
                           'front'     : self.front}

        for entity in root:
            name  = entity.find('NAME').text
            level = entity.find('LEVEL').text
            model = eval(entity.find('MODEL').text.replace('\n','').replace(' ',''))
            
            self.entities[name] = {'level' : level, 'model' : model}
    

    def add(self, name, position, layer=None):
        if name in self.entities:
            entity = self.entities[name]

            model =  entity['model']
            if layer=="player":
                self.colGrid(model, position)

            obj = {'name'  : name,
                   'level' : entity['level'], 
                   'model' : model,
                   'pos'   : position,
                   'bbox'  : collision.calcBound(model, position,self.size)}

            if not layer:
                self.entityDict[entity['level']].append(obj)
            else:
                self.entityDict[layer].append(obj)

    def getStaticGrid(self, pos, rows, cols):
        posx, posy = pos
        posx = int((posx/self.size))
        posy = int((posy/self.size))
        m = [[0 for _ in range(cols+4)] for _ in range(rows+4)] 

        for r in range(rows+4):
            for i in range(cols+4):
                try:
                    m[r][i] = self.grid[(i+posx)-2][(posy-rows+r)]
                except:
                    ''' nothing '''

        return m, (posx*self.size-2*10,posy*self.size+4*10), self.size

    def colGrid(self, model, pos):
        posx, posy = pos
        posx = int(round(float(posx)/self.size))
        posy = int(round(float(posy)/self.size))

        for r, row in enumerate(model):
            for i, element in enumerate(row):
                if element:
                    try: 
                        self.grid[i+posx][posy-len(model)+r] = True
                    except:
                        self.grid[i+posx] = {posy-len(model)+r : True } 

        #self.getStaticGrid((17,510),4,4)

    def draw(self, screen, entities):
        for entity in entities:
            try:
                m = entity['model']
                x, y  = entity['pos']
            except:
                ''' No animation found '''

            for r, row in enumerate(m):
                for i, element in enumerate(row):
                    if element:
                        pygame.draw.rect(screen, element, (int(x)+(self.size*i), int(y)+(self.size*r)-len(m)*self.size, self.size, self.size)) 


    def hitbox(self, entity):
        m = entity['model']
        return collision.Hitbox(m, entity['pos'], self.size)


