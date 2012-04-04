import pygame

class Floor():

    def __init__(self, rect, color=(120,120,120)):
        self.pos = rect # (x, y, s1, s2)
        self.color = color


    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.pos)
