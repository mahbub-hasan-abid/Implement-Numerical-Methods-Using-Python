def determinant(a1, b1, c1, a2, b2, c2, a3, b3, c3):
    return a1 * (b2 * c3 - b3 * c2) - b1 * (a2 * c3 - a3 * c2) + c1 * (a2 * b3 - a3 * b2)

print("Enter the coefficients:")

a1 = float(input("Enter a1: "))
b1 = float(input("Enter b1: "))
c1 = float(input("Enter c1: "))
d1 = float(input("Enter d1: "))

a2 = float(input("Enter a2: "))
b2 = float(input("Enter b2: "))
c2 = float(input("Enter c2: "))
d2 = float(input("Enter d2: "))

a3 = float(input("Enter a3: "))
b3 = float(input("Enter b3: "))
c3 = float(input("Enter c3: "))
d3 = float(input("Enter d3: "))

D = determinant(a1, b1, c1, a2, b2, c2, a3, b3, c3)

Dx = determinant(d1, b1, c1, d2, b2, c2, d3, b3, c3)
Dy = determinant(a1, d1, c1, a2, d2, c2, a3, d3, c3)
Dz = determinant(a1, b1, d1, a2, b2, d2, a3, b3, d3)

if D != 0:
    x = Dx / D
    y = Dy / D
    z = Dz / D

    print("Solutions:")
    print("x =", x)
    print("y =", y)
    print("z =", z)
else:
    print("The determinant is zero. So there is no unique solution.")
