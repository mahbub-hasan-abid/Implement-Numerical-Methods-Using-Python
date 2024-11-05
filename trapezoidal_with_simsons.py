import numpy as np
import matplotlib.pyplot as plt

def integrand(t):
    return 200 * np.log(140000 / (140000 - 2100 * t)) - 9.8 * t

a = 8
b = 30

h = b - a
s_approx = (h / 2) * (integrand(a) + integrand(b))
print("Approximate distance using single segment trapezoidal rule:", s_approx)

def simpson_1_3(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    s = (h / 3) * (y[0] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2]) + y[-1])
    return s

n = 100
s_true_approx = simpson_1_3(integrand, a, b, n)
E = s_true_approx - s_approx
relative_error = abs(E / s_true_approx)
print("Estimated true error:", E)
print("Estimated relative true error:", relative_error)

t = np.linspace(a, b, 100)
y = integrand(t)
plt.plot(t, y)
plt.xlabel('Time (s)')
plt.ylabel('Vertical Distance (m)')
plt.title('Vertical Distance vs. Time')
plt.grid(True)
plt.show()

table_data = np.column_stack((t, y))
print("Table of values:")
print(table_data)
