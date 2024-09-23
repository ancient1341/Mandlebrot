# 0.  From Problem Analysis to Data Definitions

I need to edit the fractal program so that it is easily reusable
The program will have a base abstract class called Fractal, to which
3 other classes are based upon Mandlebrot, Julia, and One of my choosing.

The program will also need to have Editable color gradients, which can be
selected via the command line.

# 1.  System Analysis

The program will take input from the user about which formula to run and
they will be able to add the color scheme they desire.

The User will input in the format of "python src/main.py [FRACTAL_FILE [PALETTE_NAME]]"
The program wil then open a file containing the information about the desired fractal
and will hand it to the Correct class to display it.


# 2.  Functional Examples
input
send input to fractalFactory

class fractalFactory(Julia, Mandlebrot, Other):
    def makeFractal(input):
        info = read file based upon the input

        if info Julia:
            create Julia
        if info Mandlebrot:
            create Mandlebrot
        if info other:
            create other

        create pallette based on input
        pass the pallette to the fractal class

class palletteFactory:
    def makePallette(type, iteration#):
        create PalletteClass of type
        return class

class Pallette:
    @abstract
    def getColor():
        return error message

class Fractal:
    @abstract
    def count():
        Retrun error message

    copy the code over from the 4.0 to drive the program

Class Mandelbrot:
    do the same as 4.0 with added input

# 3.  Function Template

class fractalFactory:
    pass

class Fractal:
    def count():
        pass

class Pallette:
    def getColor():
        pass

class palletteFactory:
    pass

class Mandelbrot(Fractal):
    def count(complexZ):
        pass

class Julia(Fractal):
    def count(complexZ):
        pass

class Wings(Fractal):
    def count(complexz):
        pass

class defaultGradient(Pallette):
    def getColor(iteration):
        pass    

class blackWhite(Pallette):
    def getcolor(iteration):
        pass

class thirdGradient(Pallette):
    def getColor(iteration):
        pass

# 4.  Implementation

**See Code**

# 5.  Testing

Upon initial testing if of the program it was found that whoever wrote the .frac files is a psychopath,
this is because almost every one of them is written in a slightly different format, and having based 
my program around mandelbrot.frac, it broke. I solved this problem by searching for the lowercase version
of each element through a for loop.
