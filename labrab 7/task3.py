from random import randint
import numpy as np
i = int(input('Рядочки: '))
j = int(input('Столбики: '))
m = [[randint(-10, 10) for x in range(j)] for y in range(i)]
m = np.array(m)
a = float(input('Введите число, на которое будет умножаться матрица:'))
prod = a * m
print(m)
print('/ / / / / / / / / / / / / / /')
print(prod)
