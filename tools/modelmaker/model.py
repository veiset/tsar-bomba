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
        self.name = name

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

class BoundedModel():

    def __init__(self, model):
        self.model = model
        self.name = model.name
        self.rows = model.rows
        self.cols = model.cols
        self.frames = model.frames
        self.bounds = self.bound(model)
        self.bmodel = self.boundedModel(model, self.bounds)
        self.bframes = len(self.bmodel)


    def boundedModel(self, model, bounds):
        '''
        Takes an array of matrices of colors 
        and returns a scaled array to fit the largest non-empty
        colorgrid of non empty colors.
        '''

        rows, cols, minRow, minCol = bounds
        boundedFrames = []
        for f, frame in enumerate(model.framelist):
            if not frame.isEmpty():
                boundedFrame = []
                for r in range(minRow,minRow+rows):
                    boundedFrame.append([frame.grid[r][c] for c in range(minCol, minCol+cols)])

                bframe = ColorGrid(f, rows, cols)
                bframe.grid = boundedFrame
                boundedFrames.append(bframe)

        return boundedFrames


    def bound(self, model):
        ''' 
        Takes a model and finds the smalles area (x,y grid) 
        that can represent the model.
        Returns numbers of rows and cols and row and col offsets.

        Example: (where 0 represent empty)
        Frame1      Frame2     Frame3
        0 0 0 0     0 0 0 0    0 0 0 0
        0 1 0 0     0 2 0 0    0 0 0 0
        0 0 0 0     0 2 0 0    0 3 3 0

        The smallest bound that would fit all the frames would 
        result in a 2x2 row and col grid:
        Frame1      Frame2     Frame3
        1 0         2 0        0 0
        0 0         2 0        3 3

        Giving us:
        rows = 2, cols = 2
        rowOffset = 1, colOffset = 1
        '''
        
        gMinRow, gMaxRow = (1E100,-1)
        gMinCol, gMaxCol = (1E100,-1)
        for frame in model.framelist:
            if not frame.isEmpty():
                minRow, minCol, maxRow, maxCol = self.gridBound(frame.grid)
                gMinRow = min(gMinRow, minRow)
                gMaxRow = max(gMaxRow, maxRow)
                gMinCol = min(gMinRow, minRow)
                gMaxCol = max(gMaxCol, maxCol)

        rows = (gMaxRow-gMinRow)+1
        cols = (gMaxCol-gMinCol)+1
        return (rows, cols, gMinRow, gMinCol)

    def gridBound(self, grid):
        '''
        returns the minimum and maximum points in a grid
        '''
        minRow, maxRow = (1E100,-1)
        minCol, maxCol = (1E100,-1)
        for r, rows in enumerate(grid):
            for c, col in enumerate(rows):
                if col != 0:
                    minRow = min(r, minRow)
                    maxRow = max(r, maxRow)
                    minCol = min(c, minRow)
                    maxCol = max(c, maxCol)

        return (minRow, minCol, maxRow, maxCol)

