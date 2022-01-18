import random
import numpy as np
b = []
sum = 0
n = 8
m = 8
for i in range(n):
    b.append([float(random.randint(-10, 10)) for j in range(m)])
for j in range(m):
    for i in range(n):
        if b[i][j] < 0:
            sum += b[i][j]

b = np.array(b)
print(b)
print(sum)
