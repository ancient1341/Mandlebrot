from Pallette import Pallette
class blackWhite(Pallette):
    def __init__(self, iterations):
        self.iterations = iterations
        self.WHITE = '#ffffff'
        self.BLACK = '#000000'


    def getColor(self, iteration):
        if iteration % 2 == 0:
            return self.BLACK
        else:
            return self.WHITE