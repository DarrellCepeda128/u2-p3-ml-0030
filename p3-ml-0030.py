
import numpy as np

# Cepeda Darrell
# NC: 0030
# Ejemplos de array NumPy

n0030 = np.array([10, 20, 30, 40, 50])

print(n0030)
print(n0030[0])
print(n0030[3])
print(n0030[-1])
print(n0030[-2])

print("------------------------------")

n0030 = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(n0030)
print(n0030[0, 0])
print(n0030[1, 2])
print(n0030[-1, -1])
print(n0030[-2, -2])

print("------------------------------")

# 3D array 2x2x3
n0030 = np.array([
    [
        [10, 20, 30],
        [40, 50, 60]
    ],
    [
        [70, 80, 90],
        [100, 110, 120]
    ]
])

print(n0030)
print(n0030[0, 0, 0])
print(n0030[1, 1, 1])
print(n0030[-1, -1, -2])

print("Cepeda Darrell NC = 0030")
