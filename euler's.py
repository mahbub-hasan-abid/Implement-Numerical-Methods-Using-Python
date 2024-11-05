import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def f(t, y):
    return y - (1 / 2) * np.exp(1 / 2 * t) * np.sin(5 * t) + 5 * np.exp(1 / 2 * t) * np.cos(5 * t)

def exact_solution(t):
    return (1 / 26) * (5 * np.exp(0.5 * t) * np.sin(5 * t) +
                       np.exp(0.5 * t) * (5 * np.cos(5 * t) - 1))

def euler_method(h, t_max):
    t_values = np.arange(0, t_max + h, h)
    y_values = np.zeros(len(t_values))
    y_values[0] = 0

    for i in range(1, len(t_values)):
        y_values[i] = y_values[i - 1] + h * f(t_values[i - 1], y_values[i - 1])

    return t_values, y_values

h_values = [0.1, 0.05, 0.01, 0.005, 0.001]
t_max = 5
results = []

for h in h_values:
    t_values, y_approx = euler_method(h, t_max)

    for t, approx in zip(t_values, y_approx):
        exact = exact_solution(t)
        error = approx - exact
        results.append({'h': h, 't': t, 'y_approx': approx, 'y_exact': exact, 'error': error})

comparison_df = pd.DataFrame(results)
print(comparison_df.to_string(index=False))

plt.figure(figsize=(12, 6))
for h in h_values:
    plot_data = comparison_df[comparison_df['h'] == h]
    plt.plot(plot_data['t'], plot_data['y_approx'], label=f'Euler Approximation (h={h})')

exact_t_values = np.arange(0, t_max + 0.001, 0.001)
exact_values = exact_solution(exact_t_values)
plt.plot(exact_t_values, exact_values, 'k--', label='Exact Solution', linewidth=2)

plt.title('Euler Method Approximation vs Exact Solution')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.legend()
plt.grid()
plt.show()
