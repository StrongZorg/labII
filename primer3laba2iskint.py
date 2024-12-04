import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Определение системы уравнений
def system(y, t):
    y1, y2 = y
    dydt = [y2, -y1]
    return dydt

# Начальные условия
initial_conditions = [-1, 0]

# Временные точки, на которых будет производиться численное решение
t = np.linspace(0, 2 * np.pi, 100)

# Решение системы уравнений
solution = odeint(system, initial_conditions, t)

# Извлечение решений для y1 и y2
y1_solution = solution[:, 0]
y2_solution = solution[:, 1]

# Построение графиков
plt.plot(t, y1_solution, label='y1(t)')
plt.plot(t, y2_solution, label='y2(t)')
plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.title('Решение системы дифференциальных уравнений')
plt.show()