from Pallette import Pallette
class repeatingColors(Pallette):
    def __init__(self, iterations, cycles=3):
        self.gradient = []
        self.iterations = iterations
        self.first = '#ff0000'
        self.last = '#00ff00'
        for i in range(cycles):
            self.gradient += self.createColors(int(iterations/(3*cycles)))

            self.first = self.last
            self.last = '#0000ff'

            self.gradient += self.createColors(int(iterations/(3*cycles)))

            self.first = self.last
            self.last = '#ff0000'

            self.gradient += self.createColors(int(iterations/(3*cycles)))

        for i in range(iterations-len(self.gradient)):
            self.gradient.append('#000000')

    def getColor(self, iteration):
        if iteration == self.iterations:
            return '#000000'
        else:
            return self.gradient[iteration]