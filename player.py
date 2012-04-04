import pygame

class Player():

    def __init__(self, name, pos):
        self.name      = name
        self.x, self.y = pos



    def draw(self, screen):
        model = [[0,           (255,128,0),   (242,217,193)],
                 [(255,128,0), (242,217,193), (242,217,193)],
                 [0,           (255,0,0),     (0,255,0),      (0, 255,0)],
                 [0,           (255,0,0),     (255,0,0)]]

        size = 10

        for r, row in enumerate(model):
            for i, element in enumerate(row):
                if element:
                    pygame.draw.rect(screen, element, (self.x+(size*i), self.y+(size*r), size, size)) 
