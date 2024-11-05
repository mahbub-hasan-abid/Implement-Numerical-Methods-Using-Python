import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def f(x):
    return x**2

true_value = 8.0 / 3.0

def trapezoidal_method(a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)

    integral = (h / 2) * (y[0] + 2 * sum(y[1:-1]) + y[-1])

    abs_true_error = abs(true_value - integral)
    rel_true_error = (abs_true_error / abs(true_value)) * 100

    data = {
        'x': x,
        'f(x)': y
    }
    df_table = pd.DataFrame(data)
    print(df_table.to_string(index=False))

    print(f"\nEstimated integral: {integral:.5f}")
    print(f"True value: {true_value:.5f}")
    print(f"Absolute true error: {abs_true_error:.5f}")
    print(f"Relative true error: {rel_true_error:.5f}%")

    return integral, x, y

a = 0
b = 2
n = 1

integral, x, y = trapezoidal_method(a, b, n)

plt.figure(figsize=(10, 6))
x_vals = np.linspace(a, b, 500)
y_vals = f(x_vals)

plt.plot(x_vals, y_vals, label='f(x)', color='blue')
plt.fill_between(x, 0, y, step='mid', color='lightgray', alpha=0.5, label='Trapezoids')
plt.scatter(x, y, color='red', zorder=5)

plt.title('Trapezoidal Method')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.show()
