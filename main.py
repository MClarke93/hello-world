import numpy as np

# Testing virtualenv and numpy
x = [3, 1, 2, 1, 2, 3, 2, 3, 1]
x = np.reshape(x, [3,3])
print(f"Determinant {round(np.linalg.det(x))}")
