
class LevelManager():

    def __init__(self, som):
        self.level = 0
        self.som = som


    def load(self, level):
        self.som.clear()
        self.loadStaticObjects(level)


    def loadStaticObjects(self, level):

        # Temp logic
        self.som.add('Tree01',(200,500))
        for x in range(10):
            for y in range(11): 
                self.som.add('Mountain', (x*80,y*60),'background')

        self.som.add('Tree01',(100,500),'background')
        self.som.add('House', (230,300),'background')
        self.som.add('Tree01',(450,500),'ground')
        self.som.add('Floor01',(0,520),'ground')
        self.som.add('Floor01',(100,520),'ground')
        self.som.add('Floor01',(400,520),'ground')
        self.som.add('Floor01',(600,520),'ground')
        self.som.add('Floor01',(230,320),'ground')
        self.som.add('IceTap01',(500,280),'ground')

        self.som.drawBackground()
        self.som.drawForeground()
        self.som.drawGround()

