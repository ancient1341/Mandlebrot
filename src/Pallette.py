from colour import Color

class Pallette:
    def __init__(self):
        raise NotImplementedError("Concrete subclass of Palette must implement __init__")

    def getColor(self):
        raise NotImplementedError("Concrete subclass of Palette must implement getColor()")

    def createColors(self, iterations):
        start = Color(self.first)
        temp = [c for c in start.range_to(self.last, iterations)]
        for i in range(len(temp)):
            temp[i] = temp[i].hex_l
        return temp