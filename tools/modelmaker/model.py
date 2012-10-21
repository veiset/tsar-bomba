class ColorGrid():
    '''
    '''

    def __init__(self, name="unknown", rows=20, cols=20):
        '''
        '''
        self.grid = self.new(rows, cols)
        self.rows = rows
        self.cols = cols
        self.name = name

    def setPixel(self, row, col, color):
        self.grid[row][col] = color

    def delPixel(self, row, col):
        self.grid[row][col] = 0

    def new(self, rows, cols):
        '''
        '''
        return [[0 for _ in range(cols)] for _ in range(rows)]

    def clear(self):
        '''
        '''
        self.grid = self.new(self.rows, self.cols)

    def isEmpty(self):
        for row in self.grid:
            for col in row:
                if col!=0: return False
        return True

class PixelModel():
    '''
    '''

    def __init__(self, rows=20, cols=20, frames=20, name="unknown"):
        '''
        '''
        self.rows = rows
        self.cols = cols
        self.frames = frames

        self.framelist = []
        for frame in range(frames):
            self.framelist.append(ColorGrid("frame" + str(frame), rows, cols))

    def clearAll(self):
        '''
        '''
        for frame in framelist:
            frame = frame.clear()

    def frame(self, i):
        return self.framelist[i]

    def grid(self, i):
        return self.framelist[i].grid

    def copyPreviousFrame(self, i):
        copyTab = self.framelist[i-1].grid
        self.framelist[i].grid = []
        for row in copyTab:
            self.framelist[i].grid.append(list(row))

pm = PixelModel()
print pm.rows
