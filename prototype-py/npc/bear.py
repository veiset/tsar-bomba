import npc

class Bear(npc.NPC):
    
    revModel = lambda x: [y[::-1] for y in x]

    model = {'RIGHT':[[        0,         0,             0,                0],
                     [         0,         0,             0,                0],
                     [         0,         0,             0,                0],
                     [         0,         0,     (127,32,0),               0],
                     [(127,32,0),(127,32,0),     (127,32,0),      (127,32,0)],
                     [(127,32,0),(127,32,0),     (127,32,0),               0],
                     [(127,32,0),         0,     (127,32,0),               0]],


             'STANDING_RIGHT':
                     [[(127,32,0),        0,             0,                0],
                     [(127,32,0),(127,32,0),             0,                0],
                     [(127,32,0), 0,     0,               0],
                     [(127,32,0),(127,32,0),     (127,32,0),      0],
                     [(127,32,0),  0,     0,               0],
                     [(127,32,0),(127,32,0),     0,               0]],
            }

    model['LEFT'] = revModel(model['RIGHT'])
    model['STANDING_LEFT'] = revModel(model['STANDING_RIGHT'])

    def __init__(self, name, pos):
        self.name      = name
        self.x, self.y = pos
        self.dx = self.x
        self.dy = self.y
        self.animation = 'LEFT'
        self.onGround = False

