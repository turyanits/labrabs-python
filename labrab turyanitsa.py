'''# Завдання 1. 7 Обчислити площу та периметр прямокутника, довжини сторін якого задаються.
a = int(input('Input the length of the first side:'))
b = int(input('Input the length of the second side:'))
area = a*b
perimeter = a+a+b+b
a = str(a)
b = str(b)
print("S =", area)
print('P =', perimeter)'''

#Завдання 3. Трикутник задається координатами своїх вершин на площині: . Знайти периметр трикутника.
from math import sqrt
print('Input the coordinates of the first apex:')
x1, y1 = map(float, input().split()) #
print('Input the coordinates of the second apex:')
x2, y2 = map(float, input().split())
print('Input the coordinates of the third apex:')
x3, y3 = map(float, input().split())
a = sqrt((x2-x1)**2+(y2-y1)**2)
b = sqrt((x3-x2)**2+(y3-y2)**2)
c = sqrt((x1-x3)**2+(y1-y3)**2)
p = (a+b+c)/2.0
s = sqrt(p*(p-a)*(p-b)*(p-c))
print('Area', "%.04f" % s, 'Perimeter', "%.04f" % (a+b+c))
