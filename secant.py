import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def f(x):
    return x ** 3 - 4 * x - 9

def secant_method(x0, x1, tol=1e-5, max_iter=100):
    data = []

    for i in range(max_iter):
        f_x0 = f(x0)
        f_x1 = f(x1)

        if f_x1 - f_x0 == 0:
            print("Zero denominator. No solution found.")
            return None

        x_next = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        error = np.abs(x_next - x1)
        data.append([i + 1, x0, x1, f_x0, f_x1, x_next, error])

        if error < tol:
            break

        x0, x1 = x1, x_next

    df_table = pd.DataFrame(data, columns=['Iteration', 'x0', 'x1', 'f(x0)', 'f(x1)', 'x_next', 'Error'])
    print(df_table.to_string(index=False))
    return x_next

x0 = 2.0
x1 = 3.0

root = secant_method(x0, x1)

x_vals = np.linspace(x0 - 3, x1 + 3, 500)
y_vals = f(x_vals)

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label='f(x)', color='blue')
plt.axhline(0, color='black', linewidth=0.8)
plt.scatter(root, f(root), color='red', label=f'Root at x={root:.5f}')
plt.title('Secant Method for f(x) = x^3 - 4x - 9')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.show()
