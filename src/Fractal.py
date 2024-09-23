import sys
import Factories.palletteFactory
from tkinter import Tk, Canvas, PhotoImage, mainloop
from time import time

class Fractal:
    def __init__(self):
        raise NotImplementedError("Concrete subclass of Fractal must implement __init__")
    def count(self):
        raise NotImplementedError("Concrete subclass of Fractal must implement count() method")

    def main(self, fractalName = "Fractal"):
        self.window = Tk()
        self.photo = PhotoImage(width=self.pixels, height=self.pixels)
        self.canvas = Canvas(self.window, width=self.pixels, height=self.pixels)

        # Set up the GUI so that we can display the fractal image on the screen
        self.gradient = Factories.palletteFactory.palletteFactory(self.colors, self.iterations)
        before = time()
        self.paint()

        print(f"Done in {time() - before:.3f} seconds!", file=sys.stderr)
        # Output the Fractal into a .png image
        self.photo.write(fractalName + ".png")
        print("Wrote picture " + fractalName + ".png")
        self.photo.write(fractalName + ".png")

        print("Close the image window to exit the program")
        # Call tkinter.mainloop so the GUI remains open
        mainloop()

    def alignCoords(self, type):
        if type == True:
            return ((self.centerX - (self.axisLength / 2.0)),
                    (self.centerY - (self.axisLength / 2.0)))
        else:
            return ((self.centerX + (self.axisLength / 2.0)),
                    (self.centerX + (self.axisLength / 2.0)))

    def paint(self):

        min = self.alignCoords(True)

        max = self.alignCoords(False)

        # Display the image on the screen
        self.canvas.create_image((self.pixels/2, self.pixels/2), image=self.photo, state="normal")

        # The size of a pixel at the current scale
        pixelSize = abs(max[0] - min[0]) / float(self.pixels)

        self.canvas.pack()
        for row in range(self.pixels, 0, -1):
            for col in range(self.pixels):
                x = min[0] + col * pixelSize
                y = min[1] + row * pixelSize
                iterationCount = self.count(complex(x, y))
                self.pixelColor = self.gradient.getColor(iterationCount)
                self.photo.put(self.pixelColor, (col, self.pixels - row))
            self.window.update()  # display a row of pixels


