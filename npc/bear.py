import pygame
import physics

class Bear():
    
    revModel = lambda x: [y[::-1] for y in x]

    model = {'RIGHT':[[0,             0,   (127,32,0),  0],
                     [(127,32,0),    (127,32,0), (127,32,0),  (127,32,0)],
                     [(127,32,0),              (127,32,0),     (127,32,0),      (0, 0,0)],
                     [(127,32,0),              0,     (127,32,0),      0]],
            }
    model['LEFT'] = revModel(model['RIGHT'])

    def __init__(self, name, pos):
        self.name      = name
        self.x, self.y = pos
        self.dx = self.x
        self.dy = self.y
        self.animation = 'RIGHT' 
        self.onGround = False

    def update(self, delta):

        tmp = self.dy
        self.dy = self.y

        if self.y > 500:
            self.onGround = True
        else:
            self.onGround = False

        if not self.onGround:
            self.y -= physics.gravity(self.y, tmp, delta)

    def draw(self, screen):
        m = self.model[self.animation]
        size = 15

        for r, row in enumerate(m):
            for i, element in enumerate(row):
                if element:
                    pygame.draw.rect(screen, element, (int(self.x)+(size*i), int(self.y)+(size*r), size, size)) 
