# ---------------------------------------------------------------------
print("Importing module 4.")         # Always runs when module imported

def slope(x1: float, y1: float, x2: float, y2: float) -> float:
    return (y2 - y1)/(x2 - x1)

if __name__ == "__main__":          # Runs ONLY if executed as a script
    import sys
    _, x1, y1, x2, y2 = sys.argv     # Gets four command line arguments
    print(slope(float(x1), float(y1), float(x2), float(y2)))