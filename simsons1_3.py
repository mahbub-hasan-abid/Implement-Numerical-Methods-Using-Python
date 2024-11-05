import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def f(x):
    return x**2

def simpsons_one_third_method(a, b, n):
    if n % 2 != 0:
        raise ValueError("Number of subintervals (n) must be even.")
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    integral = (h / 3) * (y[0] + 4 * sum(y[1:n:2]) + 2 * sum(y[2:n-1:2]) + y[-1])
    data = {
        'x': x,
        'f(x)': y
    }
    df_table = pd.DataFrame(data)
    print(df_table.to_string(index=False))
    return integral, x, y

a = 0
b = 2
n = 2

try:
    integral, x, y = simpsons_one_third_method(a, b, n)
    print(f"\nEstimated integral using Simpson's 1/3 method: {integral:.5f}")
except ValueError as e:
    print(e)

plt.figure(figsize=(10, 6))
x_vals = np.linspace(a, b, 500)
y_vals = f(x_vals)

plt.plot(x_vals, y_vals, label='f(x)', color='blue')
plt.fill_between(x, 0, y, step='mid', color='lightgray', alpha=0.5, label='Parabolic Segments')
plt.scatter(x, y, color='red', zorder=5)

plt.title("Simpson's 1/3 Method")
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.show()
