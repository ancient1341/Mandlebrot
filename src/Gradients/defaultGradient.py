from Pallette import Pallette
class defaultGradient(Pallette):
    def __init__(self, iterations):
        self.iterations = iterations
        self.first = '#ffe4b5'
        self.last = '#002277'

        self.gradient = self.createColors(self.iterations)

    def getColor(self, iteration):
        return self.gradient[iteration]