from Gradients.defaultGradient import *
from Gradients.blackWhite import *
from Gradients.repeatingColors import *
from Gradients.Shadows import *

def palletteFactory(color, iterations):
    if color == "default":
        gradient = defaultGradient(iterations)
    elif color == "zebra":
        gradient = blackWhite(iterations)
    elif color == 'repeating':
        gradient = repeatingColors(iterations)
    elif color == 'ghost':
        gradient = Shadows(iterations)
    else:
        print("\'" + color + "\' Is not a Color Scheme \n\n    -enter: \'default\', \'zebra\', or \'repeating\'\n")
        return color

    return gradient
