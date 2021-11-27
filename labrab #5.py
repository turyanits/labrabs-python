from math import cos
# Завдання 1. Дано натуральне число n і дійсне число x. Обчислити cos x + cos^2 x + ... cos^n x
n = 1
x = int(input("x:"))
sum = 0
for i in range(n,x):
    n+=1
    sum += cos(x)**n
   
print (sum)

# Завдання 2. Дано два натуральних числа x і y. Знайти число, яке містить найбільшу кількість нулів.
"""x = input('Перше число:')
y = input('Друге число:')
print(x.count('0')), print('- кількість нулів у першому числі.')
print(y.count('0')), print('- кількість нулів у другому числі.')

if x > y:
    print('У першому числі більше нулів.')
if x < y:
    print('У другому числі більше нулів.')
if x == y:
    print('Числа рівні')"""

# Завдання 4. Нехай  x_0 = 0, x_1 = 7, x_i = x_i(1+x_(i-2)), де i = 2,3,...
'''n = int(input('n:'))
a = 0 
b = 7  
c = 1
x = 0

while c < n:
    x = b * 2 + a
    a = b
    b = x
    c += 1
print('xn = {0}'.format(x))'''
