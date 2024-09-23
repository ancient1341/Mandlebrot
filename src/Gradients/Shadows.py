from Pallette import Pallette
class Shadows(Pallette):
    def __init__(self, iterations):
        self.iterations = iterations
        self.first = '#000000'
        self.last = '#ffffff'

        self.gradient = self.createColors(iterations)

    def getColor(self, iteration):
        #
        # if self.iterations/3 > iteration:
        #     return self.first
        # else:
        return self.gradient[iteration]