import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def f(x):
    return np.exp(-x)*((3.2*np.sin(x))-(.5*np.cos(x)))

def false_position_method(a, b, tol=1e-5, max_iter=100):
    if f(a) * f(b) >= 0:
        print("false position method fails: f(a) and f(b) must have opposite signs.")
        return None

    data = []

    for i in range(max_iter):
        c = b-((f(b)*(a-b))/(f(a)-f(b)))
        f_c=f(c)
        data.append([i + 1, a, b, c, f_c])

        if np.abs(f_c) < tol:
            break
        elif f(a) * f_c < 0:
            b = c
        else:
            a = c

    df = pd.DataFrame(data, columns=['Iteration', 'a', 'b', 'c (midpoint)', 'f(c)'])
    print(df.to_string(index=False))
    return c

a, b = 3, 4
root = false_position_method(a, b)

x_vals = np.linspace(a - 1, b + 1, 500)
y_vals = f(x_vals)

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label='f(x)')
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(root, color='red', linestyle='--', label=f'Root at x={root:.5f}')
plt.scatter(root, f(root), color='red', zorder=5)
plt.title('false position Method')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()
