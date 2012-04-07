from xml.etree import ElementTree as ET
import pygame
import collision 

class StaticObjectManager():

    def __init__(self):
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
            obj = {'name'  : name,
                   'level' : entity['level'], 
                   'model' : entity['model'],
                   'pos'   : position,
                   'bbox'  : collision.calcBound(entity['model'],position,self.size)}

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
        m = entity['model']
        return collision.Hitbox(m, entity['pos'], self.size)


