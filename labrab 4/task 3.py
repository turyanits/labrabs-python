# Завдання 3. Трикутник задається координатами своїх вершин на площині: . Знайти периметр трикутника.
from math import sqrt
print('Input the coordinates of the first apex:')
x1, y1 = map(float, input().split()) #
print('Input the coordinates of the second apex:')
x2, y2 = map(float, input().split())
print('Input the coordinates of the third apex:')
x3, y3 = map(float, input().split())
ab = (sqrt(((x1 - x2)**2)+((y1 - y2)**2)))
bc = (sqrt(((x2 - x3)**2)+((y2 - y3)**2)))
ac = (sqrt(((x1 - x3)**2)+((y1 - y3)**2)))
p = (ab+bc+ac)
print('Perimeter', p)
