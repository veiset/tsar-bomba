from pygame.locals import *

class Keypress():

    def __init__(self):
        self.key = {}
        self.lastDirection = 'RIGHT'

    def update(self,event):
        if event.type == QUIT:
            self.keys['QUIT'] = True

        elif event.type == KEYDOWN:
            
            if event.key == K_UP:
                self.key['UP'] = True
            elif event.key == K_DOWN:
                self.key['DOWN'] = True
            elif event.key == K_LEFT:
                self.key['LEFT'] = True
                self.lastDirection = 'LEFT' 
            elif event.key == K_RIGHT:
                self.key['RIGHT'] = True 
                self.lastDirection = 'RIGHT' 

        elif event.type == KEYUP:
            if event.key == K_UP:
                self.key['UP'] = False 
            elif event.key == K_DOWN:
                self.key['DOWN'] = False
            elif event.key == K_LEFT:
                self.key['LEFT'] = False
            elif event.key == K_RIGHT:
                self.key['RIGHT'] = False 

    def state(self, keyname):
        try:
            return self.key[keyname]
        except:
            return None
