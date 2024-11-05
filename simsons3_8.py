import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def f(x):
    return x**2

def simpsons_three_eighth_method(a, b, n):
    if n % 3 != 0:
        raise ValueError("Number of subintervals (n) must be a multiple of 3.")

    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)

    integral = (3 * h / 8) * (y[0] + 3 * sum(y[1:n:3]) + 3 * sum(y[2:n:3]) + 2 * sum(y[3:n-1:3]) + y[-1])

    data = {
        'x': x,
        'f(x)': y
    }
    df_table = pd.DataFrame(data)
    print(df_table.to_string(index=False))

    return integral, x, y

a = 0
b = 3
n = 3

try:
    integral, x, y = simpsons_three_eighth_method(a, b, n)
    print(f"\nEstimated integral using Simpson's 3/8 method: {integral:.5f}")
except ValueError as e:
    print(e)

plt.figure(figsize=(10, 6))
x_vals = np.linspace(a, b, 500)
y_vals = f(x_vals)

plt.plot(x_vals, y_vals, label='f(x)', color='blue')
plt.fill_between(x, 0, y, step='mid', color='lightgray', alpha=0.5, label='Simpson\'s 3/8 Segments')
plt.scatter(x, y, color='red', zorder=5)

plt.title("Simpson's 3/8 Method")
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.show()
