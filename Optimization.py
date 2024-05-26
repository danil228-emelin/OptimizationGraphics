import matplotlib.pyplot as plt
import numpy as np

# Пределы графика
x1 = np.linspace(0, 12, 400)
x2 = np.linspace(0, 12, 400)
X1, X2 = np.meshgrid(x1, x2)

# Ограничения
plt.plot(x1, (10 - x1) / 2, label='$x_1 + 2x_2 \leq 10$')
plt.plot(x1, (18 - 3*x1) / 2, label='$3x_1 + 2x_2 \leq 18$')
plt.plot(x1, x1 + 7, label='$x_1 - x_2 \geq -7$')
plt.plot(x1, x1 - 11, label='$x_1 - x_2 \leq 11$')

# Ограничение x_1, x_2 >= 0
plt.xlim(0, 12)
plt.ylim(0, 12)

# Легенда
plt.legend()

# Оси
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')

# Заголовок
plt.title('Графическое решение задачи линейного программирования')
plt.grid(True)
plt.show()
