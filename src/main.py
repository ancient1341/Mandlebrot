import sys
import Factories.fractalFactory

if len(sys.argv) < 2:
    print("\nThe correct format is: \n\n\'python src/main.py [FRACTAL_FILE [PALETTE_NAME]]\'")
    sys.exit(1)

elif len(sys.argv) < 3:
    Fractal = Factories.fractalFactory.fractalFactory(sys.argv[1])

elif len(sys.argv) < 4:
    Fractal = Factories.fractalFactory.fractalFactory(sys.argv[1], sys.argv[2])



