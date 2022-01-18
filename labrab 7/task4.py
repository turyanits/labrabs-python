# Розмістити елементи парних стовпців у порядку спадання.
import random
import numpy as np

a = []
n = int(input('Введіть кількість рядків матриці:'))
m = int(input('Введіть кількість стовпців матриці:'))
for i in range(n):
    a.append([float(random.randint(-9, 9)) for j in range(m)])
for j in range(m):
    if j % 2 != 0:
        a[j].sort()
        a = np.array(a)
print(a)
