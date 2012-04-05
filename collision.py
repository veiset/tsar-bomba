class Hitbox():

    def __init__(self, bound, size, blocksize, pos, delta=None):
        self.bound = {'left'  : bound[0],
                      'right' : bound[1],
                      'down'  : bound[2],
                      'up'    : bound[3]}
        self.rows, self.cols = size
        self.blocksize = blocksize
        self.x, self.y = pos

        if delta:
            self.dx, self.dy = delta
        else:
            self.dx = None
            self.dy = None

    def calcBound(self):
        bbox = {}

        right = []
        left = []
        up = []
        down = []

        for y, b in enumerate(self.bound['right']):
            r = (self.x+self.blocksize*self.cols)-(b*self.blocksize)
            rb = (self.y-self.blocksize*self.rows)+self.blocksize*y
            right.append((r, (rb, rb+self.blocksize)))

        for y, b in enumerate(self.bound['left']):
            r = (self.x)+(b*self.blocksize)
            rb = (self.y-self.blocksize*self.rows)+self.blocksize*y
            left.append((r, (rb, rb+self.blocksize)))

        for y, b in enumerate(self.bound['up']):
            r = (self.y)-(b*self.blocksize)
            rb = (self.x+y*self.blocksize)
            up.append((r, (rb, rb+self.blocksize)))

        for y, b in enumerate(self.bound['down']):
            r = (self.y-self.blocksize*self.rows)+(b*self.blocksize)
            rb = (self.x+y*self.blocksize)
            down.append((r, (rb, rb+self.blocksize)))

        return {'right': right, 'left': left, 'up': up, 'down': down}

def overlap(player, static):
    print player

    print player.x, player.y

    bbox = player.calcBound()
    for l in bbox['left']:
        print l

    print static

