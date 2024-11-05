import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def f(x, y):
    return x + y

x0 = 0
y0 = 1
h = 0.1
n_steps = 10

def milne_method(f, x0, y0, h, n_steps):
    x_values = [x0]
    y_values = [y0]

    for i in range(1, 4):
        x_prev = x_values[-1]
        y_prev = y_values[-1]

        k1 = h * f(x_prev, y_prev)
        k2 = h * f(x_prev + h / 2, y_prev + k1 / 2)
        k3 = h * f(x_prev + h / 2, y_prev + k2 / 2)
        k4 = h * f(x_prev + h, y_prev + k3)

        y_next = y_prev + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x_next = x_prev + h

        x_values.append(x_next)
        y_values.append(y_next)

    for i in range(3, n_steps):
        y_pred = y_values[i - 3] + (4 * h / 3) * (
                    2 * f(x_values[i], y_values[i]) - f(x_values[i - 1], y_values[i - 1]) + 2 * f(x_values[i - 2],
                                                                                                  y_values[i - 2]))

        x_next = x_values[i] + h
        y_corr = y_values[i] + (h / 3) * (
                    f(x_values[i - 2], y_values[i - 2]) + 4 * f(x_values[i], y_values[i]) + f(x_next, y_pred))

        x_values.append(x_next)
        y_values.append(y_corr)

    results = pd.DataFrame({"x": x_values, "y": y_values})
    return results

results = milne_method(f, x0, y0, h, n_steps)

print(results)

plt.figure(figsize=(10, 6))
plt.plot(results["x"], results["y"], marker='o', label="Milne's Method")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Milne's Method Solution of the ODE")
plt.legend()
plt.grid(True)
plt.show()
