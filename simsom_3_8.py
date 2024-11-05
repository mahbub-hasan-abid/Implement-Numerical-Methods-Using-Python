import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return 200 * np.log(140000 / (140000 - 2100 * x)) - 9.8 * x

def simpson_3_8_no_loop(f, a, b):
    h = (b - a) / 3
    result = (f(a) + 3 * f(a + h) + 3 * f(a + 2 * h) + f(a+3*h)) * ((b-a) / 8)
    return result

a = float(input("Enter the start of the interval (a): "))
b = float(input("Enter the end of the interval (b): "))

estimated_area = simpson_3_8_no_loop(f, a, b)

data = {
    "Start (a)": [a],
    "End (b)": [b],
    "Intervals (n)": [3],
    "Simpson's 3/8 Estimated Area": [estimated_area]
}
print(pd.DataFrame(data))

t_values = np.linspace(a, b, 100)
s_values = f(t_values)

plt.plot(t_values, s_values, label='f(t)', color='blue')
plt.fill_between(t_values, s_values, color='lightblue', alpha=0.3)
plt.xlabel('Time (t)')
plt.ylabel('f(t)')
plt.title('Function f(t) Over Time Interval [8, 30]')
plt.legend()
plt.grid(True)
plt.show()
