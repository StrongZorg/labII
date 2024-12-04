import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Определение функции, которую мы хотим аппроксимировать
def target_function(x, N):
    return np.sin((5 * np.pi * x / N) + np.sin(7 * np.pi * x / N))

# Генерация данных
N = 100  # Выберите количество точек
x_data = np.linspace(1, N, N)
y_data = target_function(x_data, N) + 0.1 * np.random.normal(size=N)  # Добавляем шум

# Определение функции для аппроксимации (в данном случае, полином 4-й степени)
def fit_function(x, a, b, c, d, e):
    return a * x**4 + b * x**3 + c * x**2 + d * x + e

# Аппроксимация данных
params, covariance = curve_fit(fit_function, x_data, y_data)

# Печать коэффициентов аппроксимации
print("Аппроксимационные коэффициенты:", params)

# Генерация данных для отображения аппроксимации
x_fit = np.linspace(1, N, 1000)
y_fit = fit_function(x_fit, *params)

# Построение графика
plt.plot(x_data, y_data, 'bo', label='Исходные данные')
plt.plot(x_fit, y_fit, 'r-', label='Аппроксимация')
plt.title('Аппроксимация функции')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
