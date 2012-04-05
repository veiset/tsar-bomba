import npc

class Police(npc.NPC):
    
    revModel = lambda x: [y[::-1] for y in x]

    model = {}
    model['RIGHT'] = [
        [ (0, 0, 238) , (0, 0, 238) , 0 , ],
        [ (238, 220, 130) , (255, 239, 219) , 0 , ],
        [ (255, 239, 219) , (255, 239, 219) , 0 , ],
        [ (0, 0, 238) , (92, 92, 92) , (92, 92, 92) , ],
        [ (0, 0, 238) , (0, 0, 238) , 0 , ],
    ]

    model['LEFT'] = revModel(model['RIGHT'])

    def __init__(self, name, pos):
        self.name      = name
        self.x, self.y = pos
        self.dx = self.x
        self.dy = self.y
        self.animation = 'LEFT'
        self.onGround = False

