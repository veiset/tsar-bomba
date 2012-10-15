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
            # Optimization (python method calls are really expensive), inlined code:
            #if (((a.top >= b.top and a.top < b.bottom) or (a.bottom <= b.bottom and a.bottom  > b.top))
            #    and
            #    ((a.left <= b.left and a.right > b.left) or (a.right >= b.right and a.left < b.right))):
            if a.intersect(b):
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


def moveable(player, cols, movex, movey, delta):
    # Collision handling
    groundTiles = []
    cilingTiles = []
    leftTiles   = []
    rightTiles  = []
   
    player.onGround = False
    player.onCiling = False
    player.blockedLeft = False
    player.blockedRight = False
    cilingMin = 0.0
    floorMin = 0.0

    for col in cols:
        a, b = col
        if a.hitsLeftOf(b) and a.xOverlap(b) < a.yOverlap(b):
            leftTiles.append(b)
            movex = 0
            player.blockedRight = True
        if a.hitsRightOf(b) and a.xOverlap(b) < a.yOverlap(b):
            rightTiles.append(b)
            movex = 0
            player.blockedLeft = True

        if a.hitsTopOf(b) and a.yOverlap(b) <= a.xOverlap(b):
            if a.xOverlap(b) > movex and a.xOverlap(b) > 2.0:
                groundTiles.append(col)
                movey = 0
                player.onGround = True
                #print (a.bottom-b.top)
                if floorMin > a.bottom-b.top:
                    floorMin = a.bottom-b.top

        if a.hitsBottomOf(b) and a.yOverlap(b) <= a.xOverlap(b):

            if a.xOverlap(b) > movex and a.xOverlap(b) > 2.0:
                cilingTiles.append(col)
                player.onCiling = True
                movey = 0
                if cilingMin < (b.bottom-a.top):
                    cilingMin = (b.bottom-a.top)

    if player.onCiling:
        player.y += cilingMin
        player.dy = player.y


    if not player.onGround:
        for col in cols:
            a, b = col
            if (a.hitsLeftOf(b) or a.hitsRightOf(b)):
                ''' '''
                try:
                    cols.remove(col)
                except:
                    ''' '''
    else:
        movey -= (-floorMin)
        player.y += movey
        player.dy = player.y
        for col in groundTiles:
            a, b = col
            if (a.hitsTopOf(b)):
                try:
                    cols.remove(col)
                except:
                    ''' tile was also a ciling '''

    for col in cols:
        a, b = col
        if a.intersect(b):
            if (a.hitsRightOf(b) or a.hitsLeftOf(b)):
                ''' '''

    if not cols:
        player.model = player.nextModel(movex,movey)

    #print len(cols), len(leftTiles), len(rightTiles), len(cilingTiles), len(groundTiles)
    player.update(delta)
    player.x += movex
    player.y += movey


