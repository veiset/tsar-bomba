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
            col = a.intersect(b)
            if col:
                cols.append(col)

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

