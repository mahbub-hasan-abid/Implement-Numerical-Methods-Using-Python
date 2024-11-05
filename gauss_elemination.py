import numpy as np

a11 = float(input("Enter coefficient a11 : "))
a12 = float(input("Enter coefficient a12 : "))
a13 = float(input("Enter coefficient a13 : "))
b1 = float(input("Enter result b1 : "))

a21 = float(input("Enter coefficient a21 : "))
a22 = float(input("Enter coefficient a22 : "))
a23 = float(input("Enter coefficient a23 : "))
b2 = float(input("Enter result b2 : "))

a31 = float(input("Enter coefficient a31 : "))
a32 = float(input("Enter coefficient a32 : "))
a33 = float(input("Enter coefficient a33 : "))
b3 = float(input("Enter result b3 : "))

A = np.array([[a11, a12, a13],
              [a21, a22, a23],
              [a31, a32, a33]])
b = np.array([b1, b2, b3])

solution = np.linalg.solve(A, b)

print("The solution is:")
print("x1 =", solution[0])
print("x2 =", solution[1])
print("x3 =", solution[2])
