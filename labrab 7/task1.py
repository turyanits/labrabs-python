# Завдання 7. Визначити добуток ДОДАТНИХ ПАРНИХ елементів матриці.

import numpy as np
from random import randint


i = int(input('Рядочки: '))
j = int(input('Столбики: '))
m = [[randint(-10, 10) for x in range(j)] for y in range(i)]
m = np.array(m)
print(m)

for elements in i:
    if 