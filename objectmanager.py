from lxml import etree
import pygame
import collision 

class StaticObjectManager():

    def __init__(self):
        self.xml = open('data/static/entities.xml','r').read()
        self.xml = etree.fromstring(self.xml)
        self.entities = {}

        self.background = []
        self.player = []
        self.front = []
        self.size = 10
        
        self.entityDict = {'background': self.background,
                           'player'    : self.player,
                           'front'     : self.front}

        for entity in self.xml.findall('ENTITY'):
            name  = entity.find('NAME').text
            level = entity.find('LEVEL').text
            model = eval(entity.find('MODEL').text.replace('\n','').replace(' ',''))
            
            self.entities[name] = {'level' : level, 'model' : model}
    

    def add(self, name, position, layer=None):
        if name in self.entities:
            entity = self.entities[name]
            obj = {'name'  : name,
                   'level' : entity['level'], 
                   'model' : entity['model'],
                   'pos'   : position}

            if not layer:
                self.entityDict[entity['level']].append(obj)
            else:
                self.entityDict[layer].append(obj)

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
        hitbox = []
        m = entity['model']
        rows = len(m)
        cols = len(m[0])


        left  = [-1 for _ in range(rows)]
        right = [-1 for _ in range(rows)]
        down  = [-1 for _ in range(cols)]
        up    = [-1 for _ in range(cols)]

        for r, row in enumerate(m):
            for c, col in enumerate(row):
                if col:
                    left[r] = c 
                    break
            for c, col in enumerate(row[::-1]):
                if col:
                    right[r] = c 
                    break

        for c in range(cols):
            for r in range(rows):
                if m[r][c]:
                    down[c] = r
                    break

            for r in range(rows):
                if m[(rows-1)-r][c]:
                    up[c] = r
                    break

        return collision.Hitbox((left, right, down, up), (rows, cols), self.size, entity['pos'])


#som = StaticObjectManager()
#som.add('Tree01', (100,200))

