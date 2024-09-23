from Fractals.Mandelbrot import Mandelbrot
from Fractals.Julia import Julia
from Fractals.Wings import Wings

def fractalFactory(file, color = 'default'):
    f = open(file, 'r')
    fileData = f.readlines()
    f.close()

    name = file[5:len(file)-5]
    print(name)

    for i in fileData:
        i = i.lower()
        if i[0] == "#":
            pass
        elif i[:4] == "type":
            type = i.split(' ')[len(i.split(' '))-1].rstrip()
        elif i[:6] == "pixels":
            pixels = int(i.split(' ')[len(i.split(' '))-1].rstrip())
        elif i[:7] == "centerx":
            centerX = float(i.split(' ')[len(i.split(' '))-1].rstrip())
        elif i[:7] == "centery":
            centerY = float(i.split(' ')[len(i.split(' '))-1].rstrip())
        elif i[:10] == "axislength":
            axisLength = float(i.split(' ')[len(i.split(' '))-1].rstrip())
        elif i[:10] == "iterations":
            iterations = int(float(i.split(' ')[len(i.split(' '))-1].rstrip()))

    if type == "mandelbrot":
        fractal = Mandelbrot(pixels, centerX, centerY, axisLength, iterations, color)
        fractal.main(fractalName=name)
    elif type == "julia":
        fractal = Julia(pixels, centerX, centerY, axisLength, iterations, color)
        fractal.main(fractalName=name)
    elif type == "wings":
        fractal = Wings(pixels, centerX, centerY, axisLength, iterations, color)
        fractal.main(fractalName=name)
    else:
        print("The inputted fractal type:\'", type, "\'is unsupported...\n\n"
              "    -This program supports [Mandelbrot], [Julia], and [Wings]\n")

