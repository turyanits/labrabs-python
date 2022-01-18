# Завдання 7. Визначити добуток ДОДАТНИХ ПАРНИХ елементів матриці.

import numpy as np
from random import randint

res = 1
a = []
n = int(input('Введіть кількість рядків матриці:'))
m = int(input('Введіть кількість стовбців матриці:'))
for i in range(n):
    a.append([float(randint(-9, 9)) for j in range(m)])
for j in range(m):
    for i in range(n):
        if a[i][j] > 0 and a[i][j] % 2 == 0:
            res *= a[i][j]
            a = np.array(a)
print(a)
print(res)
