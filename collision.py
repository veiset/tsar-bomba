import time
class Hitbox():

    def __init__(self, model, pos, size):
        self.model = model
        self.x, self.y = pos
        self.size = size

    def calcBound(self):
        boxes = []

        for x, row in enumerate(self.model):
            for y, el in enumerate(row):
                if el:
                    dx = self.x+(self.size*y)
                    dy = self.y+(self.size*x)-len(self.model)*self.size

                    boxes.append(((dx, dx+self.size),(dy,+dy+self.size)))

        return boxes


def overlap(player, static):

    bbox = player.calcBound()
    bbox2 = static.calcBound()


    for b in bbox:
        for bb in bbox2:
            m = match(b,bb)
            if m: return m


def match(bbox, bbox2):
    x, y = bbox
    x2, y2 = bbox2

    if not (x[0] > x2[1] 
            or x[1] < x2[0] 
            or y[0] > y2[1] 
            or y[1] < y2[0]):

        if ((x[0] < x2[0] and x2[0] < x[1])
            or (x[0] < x2[1] and x2[1] < x[1])):
            if y[0]-y2[0] > 5.0:
                return "UP"
            elif y[0]-y2[0] < -5.0:
                return "DOWN"
            
        if (not ((x[0] < x2[0] and x2[0] < x[1])
            or (x[0] < x2[1] and x2[1] < x[1]))
            and (x[0] <= x[1])):
            if(x[0]-x2[0] > 5.0):
                return "LEFT"
            elif (x[0]-x2[0] < -5.0):
                return "RIGHT"

    return False
