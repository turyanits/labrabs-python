# Завдання 1. 7 Обчислити площу та периметр прямокутника, довжини сторін якого задаються.
a = int(input('Input the length of the first side:'))
b = int(input('Input the length of the second side:'))
area = a*b
perimeter = a+a+b+b
a = str(a)
b = str(b)
print("S =", area)
print('P =', perimeter)