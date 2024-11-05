import numpy as np

a11 = float(input("Enter coefficient a11 (3): "))
a12 = float(input("Enter coefficient a12 (0.1): "))
a13 = float(input("Enter coefficient a13 (-0.2): "))
b1 = float(input("Enter result b1 (7.85): "))

a21 = float(input("Enter coefficient a21 (0.1): "))
a22 = float(input("Enter coefficient a22 (7): "))
a23 = float(input("Enter coefficient a23 (-0.3): "))
b2 = float(input("Enter result b2 (-19.3): "))

a31 = float(input("Enter coefficient a31 (0.3): "))
a32 = float(input("Enter coefficient a32 (-2): "))
a33 = float(input("Enter coefficient a33 (10): "))
b3 = float(input("Enter result b3 (71.4): "))

A = np.array([[a11, a12, a13, b1],
              [a21, a22, a23, b2],
              [a31, a32, a33, b3]], dtype=float)

n = len(A)
for i in range(n):
    A[i] = A[i] / A[i, i]
    for j in range(i + 1, n):
        A[j] -= A[j, i] * A[i]
print(A)

x = np.zeros(n)
for i in range(n - 1, -1, -1):
    x[i] = A[i, -1] - np.sum(A[i, i + 1:n] * x[i + 1:n])

print("Solution:")
for i in range(n):
    print(f"x{i + 1} = {x[i]}")
