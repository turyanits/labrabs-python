import math
x = float(input("Ведіть х , -p < x < p: "))
eps = float(input("Введіть точність eps= "))
sum += 0
i = 1
d = math.sin(x)
while (abs(d) > eps) & (i <= 10000):
    sum += d
    d = (-1)**i * math.sin((i+1)*x)/(i+1)
    i += 1
else:
    sum *= 2
print(sum)
if abs(x-sum) < eps:
   print('Тотожність виконується')
else:
   print('Тотожність не виконується')
