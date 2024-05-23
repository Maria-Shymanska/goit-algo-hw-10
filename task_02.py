# Завдання полягає в обчисленні значення інтеграла функції методом Монте-Карло.

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Метод Монте-Карло
N = 10000  # Кількість випадкових точок
x_random = np.random.uniform(a, b, N)
y_random = f(x_random)

# Обчислення площі під графіком
integral_mc = (b - a) * np.mean(y_random)

# Перевірка за допомогою аналітичного інтегрування з SciPy
result, error = spi.quad(f, a, b)

print("Інтеграл методом Монте-Карло: ", integral_mc)
print("Інтеграл (аналітично): ", result)
print("Абсолютна помилка: ", np.abs(integral_mc - result))

# Побудова графіка
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Випадкові точки для методу Монте-Карло
ax.scatter(x_random, y_random, s=1, color='blue', alpha=0.1)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()
