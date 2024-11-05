import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd

def f(x):
    return x**10 - 1

def false_position(a, b, tol):
    steps = []
    if f(a) * f(b) >= 0:
        print("No root in the interval.")
        return None, steps

    while True:
        root = b - (f(b) * (b - a)) / (f(b) - f(a))
        steps.append((a, b, root, f(root)))

        if abs(f(root)) < tol:
            break

        if f(a) * f(root) < 0:
            b = root
        else:
            a = root

    return root, steps

a = 0
b = 1.4
tol = 0.001

root, steps = false_position(a, b, tol)

df = pd.DataFrame(steps, columns=["a", "b", "root", "f(root)"])
print(df)

print(f"\nApproximate root: {root:.5f}")

x_vals = np.linspace(3, 4, 1000)
y_vals = [f(x) for x in x_vals]

plt.plot(x_vals, y_vals, label="f(x) = e * (3.2 sin(x) - 0.5 cos(x))")
plt.axhline(0, color="black", lw=0.5)
plt.axvline(root, color="red", linestyle="--", label=f"Root ≈ {root:.5f}")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("False Position Method Root Finding")
plt.legend()
plt.show()
