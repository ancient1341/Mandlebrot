# Fractal Visualizer User Manual

	To use the progam you must enter the command:
	
	    "py main.py [location of pattern file] [Optional Color Scheme]"

	There are many different pattern files inside the Data folder, however they are all based upon 3 different sets, the Mandelbrot, Julia, and Wings.
	If you do not enter a color scheme the program will use the default color scheme.
	
	Other than the default scheme there are three you can pick from, zebra, repeating and ghost
	
 	-'zebra' Based on iterations switches between Black and White, this scheme is white with black stripes.

 	-'repeating' This color scheme rotates through red green and blue multiple times, 
 	it is very useful for visualizing fractals with high iteration counts

 	-'ghost' This is a gradient ranging from white to black
	
	After entering in the command you should have a small box pop up and begin
	slowly rendering the pattern, Once it finishes it will save the pattern to
	[Name of Pattern].png in the same folder as main.py
	
	If this doesnt happen you may want to look at the possible errors section
	
	
# Possible Errors
	if you get an error that says:
	
	"[Errno 2] No file such file or directory" This means you mistyped the location of the .frac file

	That means you misspelled a fractal or typed one that wasnt on the list
	simply enter the correct pattern and it should work.

	If you get an error that says '[color] is not a color scheme' That means you mispelled the color scheme
	
	If you get a different error it could be because you don't have python installed, typed py main.py wrong,
	or simply have a corrupted verison
	
	
