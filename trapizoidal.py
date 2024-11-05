import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import quad

def f(t):
    return 200 * np.log(140000 / (140000 - 2100 * t)) - 9.8 * t

def trapezoidal_no_loop(f, a, b):
    h = (b - a)
    result = (f(a) + f(b)) * (h / 2)
    return result

a = float(input("Enter the start of the interval (a): "))
b = float(input("Enter the end of the interval (b): "))

trapezoidal_area = trapezoidal_no_loop(f, a, b)
s_true, _ = quad(f, a, b)
s_error = ((s_true - trapezoidal_area) / s_true) * 100

print('true value', s_true)
print('error', s_error)

table_points = np.linspace(a, b, 100)
table_value = f(table_points)
data = {'time': table_points, 'f(x)': table_value}
table_data = pd.DataFrame(data)
print('tabular formate')
print(table_data)

plt.plot(table_points, table_value)
plt.show()
