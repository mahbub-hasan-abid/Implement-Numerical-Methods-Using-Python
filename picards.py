import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import quad

def f(x, y):
    return x + y

x0 = 0
y0 = 1
h = 0.1
n_steps = 10

def picard_iteration(f, x0, y0, h, n_steps):
    x_values = [x0]
    y_values = [y0]

    for i in range(1, n_steps + 1):
        x_next = x_values[-1] + h

        def integral_func(x):
            return x + y_values[-1] + (x - x0)

        integral_approx, _ = quad(integral_func, x0, x_next)
        y_next = y0 + integral_approx
        x_values.append(x_next)
        y_values.append(y_next)

    results = pd.DataFrame({"x": x_values, "y": y_values})
    return results

results = picard_iteration(f, x0, y0, h, n_steps)

print(results)

plt.figure(figsize=(10, 6))
plt.plot(results["x"], results["y"], marker='o', label="Picard's Method")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Picard's Method Solution of the ODE")
plt.legend()
plt.grid(True)
plt.show()
