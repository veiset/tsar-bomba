import pygame
import physics

class Player():
    
    revModel = lambda x: [y[::-1] for y in x]

    model = {'RIGHT':[[0,             (255,128,0),   (242,217,193),  0],
                     [(255,128,0),    (242,217,193), (242,217,193),  0],
                     [0,              (255,0,0),     (0,255,0),      (0, 255,0)],
                     [0,              (255,0,0),     (255,0,0),      0]],


             'DOWN_RIGHT' :[[0, 0, 0, 0, 0],
                      [0, 0, 0, (255,128,0), (255,128,0)],
                      [0, (255,0,0), (255,0,0), (255,128,0), (242, 217, 193)],
                      [(255,0,0), (255,0,0), (255,0,0),0,0]]
            }
    model['LEFT'] = revModel(model['RIGHT'])
    model['DOWN_LEFT'] = revModel(model['DOWN_RIGHT'])

    def __init__(self, name, pos, keystate):
        self.name      = name
        self.x, self.y = pos
        self.dx = self.x
        self.dy = self.y
        self.animation = 'RIGHT' 
        self.onGround = False
        self.key = keystate

    def hitbox(self):
        hitbox = []
        for row in self.model[self.animation]:
            hrow = []
            for element in row:
                if element:
                    hrow.append(True)
                else:
                    hrow.append(False)
            hitbox.append(hrow)
        return hitbox

    def update(self, delta):

        tmp = self.dy
        self.dy = self.y
    
        if self.y > 500:
            self.onGround = True
        else:
            self.onGround = False

        if not self.onGround:
            self.y -= physics.gravity(self.y, tmp, delta)

        if self.key.state('RIGHT'):
            if self.key.state('DOWN'):
                self.x += 1.0
            else:
                self.x += 2.0

        if self.key.state('LEFT'):
            if self.key.state('DOWN'):
                self.x -= 1.0
            else:
                self.x -= 2.0
        
        if self.key.state('UP'):
            if self.onGround:
                self.y -= 5
            if self.animation == 'DOWN_RIGHT':
                self.animation = 'RIGHT'
            if self.animation == 'DOWN_LEFT':
                self.animation = 'LEFT'

        if self.key.state('DOWN'):
            if self.onGround: 
                if self.key.lastDirection == 'RIGHT':
                    self.animation = 'DOWN_RIGHT'
                else:
                    self.animation = 'DOWN_LEFT'

        elif self.key.state('RIGHT'):
            self.animation = 'RIGHT'
        elif self.key.state('LEFT'):
            self.animation = 'LEFT'
        

    def draw(self, screen):
        m = self.model[self.animation]
        size = 10

        for r, row in enumerate(m):
            for i, element in enumerate(row):
                if element:
                    pygame.draw.rect(screen, element, (int(self.x)+(size*i), int(self.y)+(size*r), size, size)) 
