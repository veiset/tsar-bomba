import pygame
import physics

class Moose():
    revModel = lambda x: [y[::-1] for y in x]

    model = {}
    model['LEFT'] = [[ 0 , (255, 160, 122) , 0 , 0 , 0 , 0 , 0 , ],
                    [ 0 , 0 , (255, 160, 122) , 0 , 0 , 0 , 0 , ],
                    [ 0 , (255, 160, 122) , 0 , 0 , 0 , 0 , 0 , ],
                    [ 0 , (139, 62, 47) , (139, 62, 47) , (139, 62, 47) , (139, 62, 47) , 0 , 0 , ],
                    [ (139, 62, 47) , (139, 62, 47) , (139, 62, 47) , (139, 62, 47) , (139, 62, 47) , (139, 62, 47) , (139, 62, 47) , ],
                    [ 0 , 0 , (139, 62, 47) , (139, 62, 47) , (139, 62, 47) , (139, 62, 47) , (139, 62, 47) , ],
                    [ 0 , 0 , (139, 62, 47) , 0 , 0 , 0 , (139, 62, 47) , ],
                    [ 0 , (139, 62, 47) , (139, 62, 47) , 0 , 0 , (139, 62, 47) , (139, 62, 47) , ],]

    model['RIGHT'] = revModel(model['LEFT'])


    def __init__(self, name, pos):
        self.name      = name
        self.x, self.y = pos
        self.dx = self.x
        self.dy = self.y
        self.animation = 'LEFT'
        self.onGround = False

    def update(self, delta):

        tmp = self.dy
        self.dy = self.y
        if self.y > 400:
            self.onGround = True

        if not self.onGround:
            self.y -= physics.gravity(self.y, tmp, delta)

    def draw(self, screen):
        m = self.model[self.animation]
        size = 15

        for r, row in enumerate(m):
            for i, element in enumerate(row):
                if element:
                    pygame.draw.rect(screen, element, (int(self.x)+(size*i), int(self.y)+(size*r), size, size)) 

