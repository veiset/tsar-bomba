from lxml import etree
import pygame

class StaticObjectManager():

    def __init__(self):
        self.xml = open('data/static/entities.xml','r').read()
        self.xml = etree.fromstring(self.xml)
        self.entities = {}

        self.background = []
        self.player = []
        self.front = []
        
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
            size = 10

            for r, row in enumerate(m):
                for i, element in enumerate(row):
                    if element:
                        pygame.draw.rect(screen, element, (int(x)+(size*i), int(y)+(size*r)-len(m)*10, size, size)) 



#som = StaticObjectManager()
#som.add('Tree01', (100,200))

