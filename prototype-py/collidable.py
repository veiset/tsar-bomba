

class Collidable():
    '''
    boundedbox (top,bottom,left,right)    
    boundedbox.intersect(boundedBox2)
    '''


    def intersect(self, b):
        '''
        b  -- boundedbox of collidable entity
        '''

        #return ( (self.hitsBottomOf(b) or self.hitsTopOf(b)) and ( self.hitsLeftOf(b) or self.hitsRightOf(b)))

        return (((self.top >= b.top and self.top  < b.bottom) or (self.bottom <= b.bottom and self.bottom  > b.top))
                and
                ((self.left <= b.left and self.right > b.left) or (self.right >= b.right and self.left   < b.right)))


    def xOverlap(self, b):
        if (self.hitsTopOf(b) or self.hitsBottomOf(b)):
            if self.hitsLeftOf(b):
                return self.right - b.left

            elif self.hitsRightOf(b):
                return b.right - self.left

        return 0.0

    def yOverlap(self, b):
        if (self.hitsLeftOf(b) or self.hitsRightOf(b)):

            if self.hitsTopOf(b):
                return self.bottom - b.top

            elif self.hitsBottomOf(b):
                return b.bottom - self.top

        return 0.0

    def hitsTopOf(self, b):
        '''
        ______
        | a  |
        |____|_
        || b  |
         |    |
         |____|
        '''
        return (self.bottom <= b.bottom and
            self.bottom  > b.top)

    def hitsBottomOf(self, b):
        '''
        ______
        | b  |
        |____|_
        || a  |
         |    |
         |____|
        '''
        return (self.top >= b.top and
            self.top  < b.bottom)

    def hitsLeftOf(self, b):
        '''
          ______
        __|_b_ |
        | a  | |
        |    |_|
        |____|
        '''
        return (self.left <= b.left and
            self.right > b.left)

    def hitsRightOf(self, b):
        '''
          ______
        __|_a  |
        | b  | |
        |    |_|
        |____|
        '''
        return (self.right >= b.right and
            self.left   < b.right)

class BoundedBox(Collidable):

    def __init__(self, left, right, top, bottom):
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom


