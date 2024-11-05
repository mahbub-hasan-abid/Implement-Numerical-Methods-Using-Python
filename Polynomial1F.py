import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

np.random.seed(42)
n = 78
age = np.random.uniform(1, 10, n)
length = 5 + 10 * age - 0.5 * age**2 + np.random.normal(0, 2, n)

data = pd.DataFrame({'Age': age, 'Length': length})

degree = 2
poly_features = PolynomialFeatures(degree=degree)
X_poly = poly_features.fit_transform(data[['Age']])
y = data['Length']

model = LinearRegression()
model.fit(X_poly, y)

y_pred = model.predict(X_poly)

results_df = pd.DataFrame({
    'Age': data['Age'],
    'Actual Length': y,
    'Predicted Length': y_pred,
    'Residual (Error)': y - y_pred
})

pd.set_option('display.float_format', '{:.2f}'.format)
print(results_df)

mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)

print(f'\nMean Squared Error (MSE): {mse:.2f}')
print(f'R-squared (R2): {r2:.2f}')

plt.figure(figsize=(12, 6))
plt.scatter(data['Age'], data['Length'], color='blue', label='Actual Data')
age_range = pd.DataFrame(np.linspace(data['Age'].min(), data['Age'].max(), 100), columns=['Age'])
age_range_poly = poly_features.transform(age_range)
length_pred = model.predict(age_range_poly)
plt.plot(age_range, length_pred, color='red', label=f'Polynomial Regression (degree {degree})')

plt.title('Polynomial Regression: Fish Length vs Age')
plt.xlabel('Age (years)')
plt.ylabel('Length (mm)')
plt.legend()
plt.grid(True)
plt.show()
