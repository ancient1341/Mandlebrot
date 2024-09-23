from Fractal import Fractal

class Julia(Fractal):
    def __init__(self, pixels, centerX, centerY, axisLength, iterations, colors):
        self.pixels = pixels
        self.centerX = centerX
        self.centerY = centerY
        self.axisLength = axisLength
        self.iterations = iterations
        self.colors = colors


    def count(self, complexZ):
        for i in range(self.iterations):
            complexZ = complexZ * complexZ + complex(-1, 0)  # Iteratively compute z1, z2, z3 ...
            if abs(complexZ) > 2:
                return i  # The sequence is unbounded

        return self.iterations-1