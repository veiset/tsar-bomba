from model import BoundedModel, PixelModel
import json

def modelToJson(model):
    model = BoundedModel(model)
    mjson = json.dumps(
                {"name" : model.name,
                 "bounds" : {"rows" : model.bounds[0],
                             "cols" : model.bounds[1],
                             "rowOffset" : model.bounds[2],
                             "colOffset" : model.bounds[3],
                             "frames:" : model.bframes
                             },
                 "size" : {"rows" : model.rows,
                           "cols" : model.cols,
                           "frames" : model.frames
                          }
                 },indent=4)

    # avoid indenting the frames to make the json human readable
    mjson = mjson[:-2] + ",\n    " + json.dumps({
        "frames" : [{frame.name : frame.grid} for frame in model.bmodel]})[1:-1] + "\n}"

    return mjson

def jsonToModel(mjson):
    data = json.loads(mjson)

    rows = data["size"]["rows"]
    cols = data["size"]["cols"]
    numberOfFrames = data["size"]["frames"]
    frames = data["frames"]
    name = data["name"]
    rowOffset = data["bounds"]["rowOffset"]
    colOffset = data["bounds"]["colOffset"]

    model = PixelModel(rows, cols, numberOfFrames, name)
    for frame in frames:
        for name, grid in frame.iteritems():
            colorgrid = model.frame(int(name))
            for r, row in enumerate(grid):
                for c, col in enumerate(row):
                    if col != 0:
                        colorgrid.setPixel(r+rowOffset, c+colOffset, tuple(col))

    return model

