import pygame
import physics

class NPC():

    def update(self, delta):

        tmp = self.dy
        self.dy = self.y

        if self.y > 350:
            self.onGround = True

        if not self.onGround:
            self.y -= physics.gravity(self.y, tmp, delta)

    def draw(self, screen):
        try:
            m = self.model[self.animation]
        except:
            ''' No animation found '''
        size = 10

        for r, row in enumerate(m):
            for i, element in enumerate(row):
                if element:
                    pygame.draw.rect(screen, element, (int(self.x)+(size*i), int(self.y)+(size*r), size, size)) 

