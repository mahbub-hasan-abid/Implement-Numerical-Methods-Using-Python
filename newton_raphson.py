import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def f(x):
    return x ** 3 - 4 * x - 9

def df(x):
    return 3 * x ** 2 - 4

def newton_raphson(x0, tol=1e-5, max_iter=100):
    data = []
    x_prev = x0

    for i in range(max_iter):
        f_x = f(x_prev)
        df_x = df(x_prev)

        if df_x == 0:
            print("Derivative is zero. No solution found.")
            return None

        x_next = x_prev - f_x / df_x
        error = np.abs(x_next - x_prev)
        data.append([i + 1, x_prev, f_x, x_next, error])

        if error < tol:
            break
        x_prev = x_next

    df_table = pd.DataFrame(data, columns=['Iteration', 'x_prev', 'f(x)', 'x_next', 'Error'])
    print(df_table.to_string(index=False))
    return x_next

x0 = 2.0

root = newton_raphson(x0)

x_vals = np.linspace(x0 - 3, x0 + 3, 500)
y_vals = f(x_vals)

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label='f(x)', color='blue')
plt.axhline(0, color='black', linewidth=0.8)
plt.scatter(root, f(root), color='red', label=f'Root at x={root:.5f}')
plt.title('Newton-Raphson Method for f(x) = x^3 - 4x - 9')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.show()
