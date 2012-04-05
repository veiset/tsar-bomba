import pygame
import physics
import random
import collision 

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
        self.blocked = {'LEFT' : False,
                        'RIGHT': False,
                        'DOWN' : False, 
                        'UP'   : False}
        self.key = keystate
        self.size = 10

    def direction(self):
        direction = {'RIGHT': False, 'LEFT': False, 'UP': False, 'DOWN': False}
        if (self.x>self.dx):
            direction['RIGHT'] = True
        if (self.x<self.dx):
            direction['LEFT'] = True
        if (self.y<self.dy):
            direction['UP'] = True
        if (self.y>self.dy):
            direction['DOWN'] = True

        return direction

    def hitbox(self):

        return collision.Hitbox(self.model[self.animation], (self.x, self.y), self.size)

    def update(self, delta):

        tmp = self.dy
        self.dy = self.y
        self.dx = self.x
    
        if self.y >= 500:
            self.y = 500
            self.blocked['DOWN'] = True
        else:
            self.blocked['DOWN'] = False

        if not self.blocked['DOWN']:
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
            if self.blocked['DOWN']:
                self.y -= 5
            if self.animation == 'DOWN_RIGHT':
                self.animation = 'RIGHT'
            if self.animation == 'DOWN_LEFT':
                self.animation = 'LEFT'

        if self.key.state('DOWN'):
            if self.blocked['DOWN']:
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
        
        #wobbleWobble = random.choice([0,1,-1])
        #nobbleWobble = random.choice([0,1])

        # Just for fun. This looks very stupid!
       # if self.key.state('LEFT') or self.key.state('RIGHT'):
       #     for r, row in enumerate(m[:-1]):
       #         for i, element in enumerate(row):
       #             if element:
       #                 pygame.draw.rect(screen, element, (int(self.x)+(size*i)+wobbleWobble, int(self.y)+(size*r)+nobbleWobble-len(m)*size, size, size)) 

       #     for i, element in enumerate(m[len(m)-1]):
       #         if element:
       #             pygame.draw.rect(screen, element, (int(self.x)+(size*i), int(self.y)+(size*(len(m)-1))-len(m)*size, size, size)) 

       # else:
        for r, row in enumerate(m):
            for i, element in enumerate(row):
                if element:
                    pygame.draw.rect(screen, element, (int(self.x)+(self.size*i), int(self.y)+(self.size*r)-len(m)*self.size, self.size, self.size)) 
        
