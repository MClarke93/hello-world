# ---------------------------------------------------------------------
print("Importing module 5.")         # Always runs when module imported

from math import sqrt               # Importing from an builtin library
def distance(x1: float, y1: float, x2: float, y2: float) -> float:
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

if __name__ == "__main__":          # Runs ONLY if executed as a script
    import sys
    _, x1, y1, x2, y2 = sys.argv     # Gets four command line arguments
    print(distance(float(x1), float(y1), float(x2), float(y2)))