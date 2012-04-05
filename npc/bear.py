import pygame
import physics

class Bear():
    
    revModel = lambda x: [y[::-1] for y in x]

    model = {'RIGHT':[[        0,         0,             0,                0],
                     [         0,         0,             0,                0],
                     [         0,         0,             0,                0],
                     [         0,         0,     (127,32,0),               0],
                     [(127,32,0),(127,32,0),     (127,32,0),      (127,32,0)],
                     [(127,32,0),(127,32,0),     (127,32,0),               0],
                     [(127,32,0),         0,     (127,32,0),               0]],


             'STANDING_RIGHT':
                     [[(127,32,0),        0,             0,                0],
                     [(127,32,0),(127,32,0),             0,                0],
                     [(127,32,0), 0,     0,               0],
                     [(127,32,0),(127,32,0),     (127,32,0),      0],
                     [(127,32,0),  0,     0,               0],
                     [(127,32,0),(127,32,0),     0,               0]],
            }

    model['LEFT'] = revModel(model['RIGHT'])
    model['STANDING_LEFT'] = revModel(model['STANDING_RIGHT'])

    def __init__(self, name, pos):
        self.name      = name
        self.x, self.y = pos
        self.dx = self.x
        self.dy = self.y
        self.animation = 'STANDING_RIGHT' 
        self.onGround = False

    def update(self, delta):

        tmp = self.dy
        self.dy = self.y

        if not self.onGround:
            self.y -= physics.gravity(self.y, tmp, delta)

    def draw(self, screen):
        m = self.model[self.animation]
        size = 15

        for r, row in enumerate(m):
            for i, element in enumerate(row):
                if element:
                    pygame.draw.rect(screen, element, (int(self.x)+(size*i), int(self.y)+(size*r), size, size)) 
