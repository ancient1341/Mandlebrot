from Fractal import Fractal

class Wings(Fractal):
    def __init__(self, pixels, centerX, centerY, axisLength, iterations, colors):
        self.pixels = pixels
        self.centerX = centerX
        self.centerY = centerY
        self.axisLength = axisLength
        self.iterations = iterations
        self.colors = colors


    def count(self, complexZ):
            c = complex(0, 0)

            for i in range(self.iterations):
                c = c**c + complexZ  # Get c1, c2, ...
                if abs(c) > 2:
                    return i
            return self.iterations-1