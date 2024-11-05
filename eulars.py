import numpy as np
import matplotlib.pyplot as plt

def dy_dt(t, y):
    return y + (-0.5 * np.exp(t / 2) * np.sin(5 * t) + 5 * np.exp(t/5) * np.cos(5 * t))

def euler_method(dy_dt, h):
    t_values = []
    y_values = []
    t = 0
    y = 0
    while t < 5:
        y += h * dy_dt(t, y)
        t += h
        t_values.append(t)
        y_values.append(y)
    return t_values, y_values

step_sizes = [0.1, 0.05, 0.01, 0.005, 0.001]
solutions = []

for h in step_sizes:
    t_values, y_values = euler_method(dy_dt, h)
    solutions.append((h, t_values, y_values))

plt.figure(figsize=(10, 6))
for h, t_values, y_values in solutions:
    plt.plot(t_values, y_values, label=f"h = {h}")
plt.xlabel("t")
plt.ylabel("y(t)")
plt.title("Euler's Method: Approximation of y(t) for Different Step Sizes")
plt.legend()
plt.grid(True)
plt.show()
