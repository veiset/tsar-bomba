import pygame

class Player():

    model = {'RIGHT':[[0,             (255,128,0),   (242,217,193),  0],
                     [(255,128,0),    (242,217,193), (242,217,193),  0],
                     [0,              (255,0,0),     (0,255,0),      (0, 255,0)],
                     [0,              (255,0,0),     (255,0,0),      0]],

             'LEFT' :[[0,             (242,217,193), (255,128,0),    0],
                     [0,              (242,217,193), (242,217,193),  (255,128,0)],
                     [(0,255,0),      (0,255,0),     (255,0,0),      0],
                     [0,              (255,0,0),     (255,0,0),      0]]
            }

    def __init__(self, name, pos):
        self.name      = name
        self.x, self.y = pos
        self.animation = 'RIGHT' # 'LEFT' / 'RIGHT' / 'UP' / 'DOWN'

    def draw(self, screen):
        m = self.model[self.animation]
        size = 10

        for r, row in enumerate(m):
            for i, element in enumerate(row):
                if element:
                    pygame.draw.rect(screen, element, (self.x+(size*i), self.y+(size*r), size, size)) 
