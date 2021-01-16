import math


class NodeData:
    key = 0
    info = 0
    tag = 0
    pos = 0.0
    weight = 0


    def __init__(self, key, pos: tuple()):
        self.key = key
        self.pos = pos
        self.distance = math.inf
        self.previous = NodeData
        self.visited = False
        # NodeData.key = self.key + 1

    def getkey(self):
        return self.key

    def getinfo(self):
        return self.info

    def setinfo(self, value):
        self.info = value

    def gettag(self):
        return self.tag

    def settag(self, value):
        self.tag = value

    def get_pos(self):
        return self.pos

    def __str__(self):
        return str(self.key) + " " + str(self.pos) + " " + str(self.tag)
