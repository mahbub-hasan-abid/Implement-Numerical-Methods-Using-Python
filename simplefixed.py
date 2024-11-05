import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def g(x):
    return np.cos(x)

def fixed_point_iteration(x0, tol=1e-5, max_iter=100):
    data = []
    x_prev = x0

    for i in range(max_iter):
        x_next = g(x_prev)
        data.append([i + 1, x_prev, x_next, np.abs(x_next - x_prev)])

        if np.abs(x_next - x_prev) < tol:
            break
        x_prev = x_next

    df = pd.DataFrame(data, columns=['Iteration', 'x_prev', 'x_next', 'Error'])
    print(df.to_string(index=False))
    return x_next

x0 = 0.5

root = fixed_point_iteration(x0)

x_vals = np.linspace(-1, 2, 500)
y_vals = g(x_vals)

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label='g(x)', color='blue')
plt.plot(x_vals, x_vals, label='y = x', color='green', linestyle='--')
plt.scatter(root, g(root), color='red', label=f'Fixed Point at x={root:.5f}')
plt.title('Fixed-Point Iteration Method')
plt.xlabel('x')
plt.ylabel('g(x)')
plt.grid(True)
plt.legend()
plt.show()
