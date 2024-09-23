#!/bin/env python3

# Julia Set Visualizer

import sys
from tkinter import Tk, Canvas, PhotoImage, mainloop
from time import time

class Fractal:
    def __init__(self):

        self.window = Tk()
        self.photo = PhotoImage(width=512, height=512)
        self.canvas = Canvas(self.window, width=512, height=512)

        #the locations and size of the patterns
        self.sets = {
            'fulljulia': {
                'centerX': 0.0,
                'centerY': 0.0,
                'axisLength': 4.0,
            },

            'hourglass': {
                'centerX': 0.618,
                'centerY': 0.00,
                'axisLength': 0.017148277367054,
            },

            'lakes': {
                'centerX': -0.339230468501458,
                'centerY': 0.417970758224314,
                'axisLength': 0.164938488846612,
            },

            'mandelbrot': {
                'centerX': -0.6,
                'centerY': 0.0,
                'axisLength': 2.5,
            },

            'spiral0': {
                'centerX': -0.761335372924805,
                'centerY': 0.0835704803466797,
                'axisLength': 0.004978179931102462,
            },

            'spiral1': {
                'centerX': -0.747,
                'centerY': 0.1075,
                'axisLength': 0.002,
            },

            'seahorse': {
                'centerX': -0.745,
                'centerY': 0.105,
                'axisLength': 0.01,
            },

            'elephants': {
                'centerX': 0.30820836067024604,
                'centerY': 0.030620936230004017,
                'axisLength': 0.03,
            },

            'leaf': {
                'centerX': -1.543577002,
                'centerY': -0.000058690069,
                'axisLength': 0.000051248888,
            },
        }

        ## the color gradient
        self.gradient = [
            '#ffe4b5', '#ffe5b2', '#ffe7ae', '#ffe9ab', '#ffeaa8', '#ffeda4',
            '#ffefa1', '#fff29e', '#fff49a', '#fff797', '#fffb94', '#fffe90',
            '#fcff8d', '#f8ff8a', '#f4ff86', '#f0ff83', '#ebff80', '#e7ff7c',
            '#e2ff79', '#ddff76', '#d7ff72', '#d2ff6f', '#ccff6c', '#c6ff68',
            '#bfff65', '#b9ff62', '#b2ff5e', '#abff5b', '#a4ff58', '#9dff54',
            '#95ff51', '#8dff4e', '#85ff4a', '#7dff47', '#75ff44', '#6cff40',
            '#63ff3d', '#5aff3a', '#51ff36', '#47ff33', '#3eff30', '#34ff2c',
            '#2aff29', '#26ff2c', '#22ff30', '#1fff34', '#1cff38', '#18ff3d',
            '#15ff42', '#11ff47', '#0eff4c', '#0bff51', '#07ff57', '#04ff5d',
            '#01ff63', '#00fc69', '#00f970', '#00f677', '#00f27d', '#00ef83',
            '#00ec89', '#00e88e', '#00e594', '#00e299', '#00de9e', '#00dba3',
            '#00d8a7', '#00d4ab', '#00d1af', '#00ceb3', '#00cab7', '#00c7ba',
            '#00c4be', '#00c0c0', '#00b7bd', '#00adba', '#00a4b6', '#009cb3',
            '#0093b0', '#008bac', '#0082a9', '#007ba6', '#0073a2', '#006b9f',
            '#00649c', '#005d98', '#005695', '#004f92', '#00498e', '#00438b',
            '#003d88', '#003784', '#003181', '#002c7e', '#00277a', '#002277',
        ]


    def fractal_main(self, fractal, isJulia):
        # Set up the GUI so that we can display the fractal image on the screen
        before = time()
        self.isJulia = isJulia
        self.paint(self.sets[fractal])

        print(f"Done in {time() - before:.3f} seconds!", file=sys.stderr)
        # Output the Fractal into a .png image
        self.photo.write(fractal + ".png")
        print("Wrote picture " + fractal + ".png")
        self.photo.write(fractal + ".png")

        print("Close the image window to exit the program")
        # Call tkinter.mainloop so the GUI remains open
        mainloop()

    def alignCoords(self, set, type):
        if type == True:
            return ((set['centerX'] - (set['axisLength'] / 2.0)),
               (set['centerY'] - (set['axisLength'] / 2.0)))
        else:
            return ((set['centerX'] + (set['axisLength'] / 2.0)),
               (set['centerY'] + (set['axisLength'] / 2.0)))

    def paint(self, set):  ## False is mandelbrot
        """Paint a Fractal image into the TKinter PhotoImage canvas.
        Assumes the image is 512x512 pixels."""

        min = self.alignCoords(set, True)

        max = self.alignCoords(set, False)

        # Display the image on the screen
        self.canvas.create_image((256, 256), image=self.photo, state="normal")

        # The size of a pixel at the current scale
        pixelSize = abs(max[0] - min[0]) / 512.0

        self.canvas.pack()
        for row in range(512, 0, -1):
            for col in range(512):
                x = min[0] + col * pixelSize
                y = min[1] + row * pixelSize
                color = self.getColorFromPallette(complex(x, y))
                self.photo.put(color, (col, 512 - row))
            self.window.update()  # display a row of pixels



    def getColorFromPallette(self, z):
        """Return the index of the color of the current pixel within the Julia set
        in the palette array"""
        if self.isJulia:
            for i in range(len(self.gradient)):
                z = z * z + complex(-1, 0)  # Iteratively compute z1, z2, z3 ...
                if abs(z) > 2:
                    return self.gradient[i]  # The sequence is unbounded
                    z += z + sets['c']

            return self.gradient[len(self.gradient) - 1]
        else:
            c = complex(0, 0)

            for i in range(len(self.gradient)):
                c = c * c + z  # Get c1, c2, ...
                if abs(c) > 2:
                    return self.gradient[i]
            return self.gradient[len(self.gradient) - 1]


    def getFractalConfiguration(self, name): ## returns a value from a dictionary
        if name in self.set:
            return name



if __name__ == '__main__':
    # Process command-line arguments, allowing the user to select their fractal
    if len(sys.argv) < 2:
        print("Please provide the name of a fractal as an argument")
        for i in Fractal.sets:
            print(f"\t{i}")
        sys.exit(1)

    elif sys.argv[1] not in Fractal.sets:
        print(f"ERROR: {sys.argv[1]} is not a valid fractal")
        print("Please choose one of the following:")
        for i in Fractal.sets:
            print(f"\t{i}")
        sys.exit(1)

    else:
        fratcal_config = Fractal.getFractalConfiguration(sys.argv[1])
        Fractal.fractal_main(fratcal_config)
