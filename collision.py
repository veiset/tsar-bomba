import time
import objectmanager
import collidable

def collision(al, bl):
    '''
    Match a two lists of collidable entities

    Keyword arguments:
    al -- list one (a)
    bl -- list two (b)
    '''
    cols = []


    for a in al:
        for b in bl:
            if (((a.top >= b.top and a.top < b.bottom) or (a.bottom <= b.bottom and a.bottom  > b.top))
                and
                ((a.left <= b.left and a.right > b.left) or (a.right >= b.right and a.left < b.right))):
            #if a.intersect(b):
                cols.append((a,b))

    return cols

def calcBound(model, pos, blocksize):
    boxes = []
    posx, posy = pos

    for x, row in enumerate(model):
        for y, el in enumerate(row):
            if el:
                dx = posx+(blocksize*y)
                dy = posy+(blocksize*x)-len(model)*blocksize
                boxes.append(collidable.BoundedBox(dx, dx+blocksize, dy, dy+blocksize))

    return boxes

