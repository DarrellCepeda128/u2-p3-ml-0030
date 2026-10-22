import numpy as np
# Cepeda Darrell Nc = 0030 Fecha 22/03/2026
# Mas ejemplos de array Numerical Python
n0030= np.array([10, 20, 30, 40, 50])

print(n0030)
print(n0030[0])
print(n0030[3])
print(n0030[-1])
print(n0030[-2])
print("-------------------------------- ")
n0030 = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print(n0030)
print(n0030[0, 0])
print(n0030[1, 2])
print(n0030[-1, -1])
print(n0030[-2, -2])
print("--------------------------------- ")
# 3D array 2x(2x3)
n0300 = np.array([
#0
    [
        [10, 20, 30],
        [40, 50, 60]
    ],
#1
    [
        [70, 80, 90],
        [100, 110, 120]
    ]
])
print(n0030)
print(n0030[0, 0, 0])
print(n0030[1, 1, 2])
print(n0030[-1, -1, -2])
print("Cepeda Darrell NC = 0030")