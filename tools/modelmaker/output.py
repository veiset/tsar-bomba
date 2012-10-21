
def json(modelGrid):
    '''
    Takes an array of matrices of colors 
    and outputs a JSON scaled to fit the largest non-empty
    colorgrid of non empty colors.
    '''
    print "..."

def outputModel(model):
    print '---- COPY & PASTE -----'
    mx = 0
    my = 0
    for x, row in enumerate(model):
        for y, el in enumerate(row):
            if el and y > my:
                my = y
            if el and x > mx:
                mx = x
    mx += 1
    my += 1

    print "    <ENTITY>"
    print "        <NAME>EditMe</NAME>"
    print "        <MODEL>"
    print "[",
    for y in range(my):
        print "[",
        for x in range(mx):
            print model[x][y],",",
        print "],"
    print "]"
    print "        </MODEL>"
    print "    </ENTITY>"

