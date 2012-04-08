import npc

class Dino(npc.NPC):
    
    revModel = lambda x: [y[::-1] for y in x]

    model = {}
    model['RIGHT'] = [
        [ 0 , 0 , 0 , 0 , 0 , 0 , (69, 139, 0) , 0 , ],
        [ 0 , 0 , 0 , 0 , 0 , (35, 142, 35) , (0, 100, 0) , (69, 139, 0) , ],
        [ 0 , 0 , 0 , 0 , (35, 142, 35) , (69, 139, 0) , (247, 247, 247) , (240, 240, 240) , ],
        [ 0 , 0 , 0 , (35, 142, 35) , (69, 139, 0) , (69, 139, 0) , (69, 139, 0) , (69, 139, 0) , ],
        [ 0 , 0 , (35, 142, 35) , (69, 139, 0) , (69, 139, 0) , (69, 139, 0) , 0 , 0 , ],
        [ 0 , (35, 142, 35) , (69, 139, 0) , (69, 139, 0) , (69, 139, 0) , 0 , 0 , 0 , ],
        [ (35, 142, 35) , (69, 139, 0) , 0 , 0 , (69, 139, 0) , (69, 139, 0) , 0 , 0 , ],
    ]


    model['LEFT'] = revModel(model['RIGHT'])

    def __init__(self, name, pos):
        self.name      = name
        self.x, self.y = pos
        self.dx = self.x
        self.dy = self.y
        self.animation = 'LEFT'
        self.onGround = False

