# Дана цілочислова матриця 8×8. Знайти такі k, що k-й рядок матриці співпадає з k-м стовбцем.
import random
import numpy as np

b = []
count = 0
n = 8
m = 8
for i in range(n):
    b.append([float(random.randint(-10, 10)) for j in range(m)])
for j in range(m):
    for i in range(n):
        if b[i] == b[j]:
            count += 1
b = np.array(b)
print(b)
print('Кількість = {0}'.format(m - count))