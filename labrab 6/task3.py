# Дано два вектори x,y Є R^n. З’ясувати, чи є вони перпендикулярними.
print('Введите координаты первого вектора:')
x1, y1 = map(float, input().split())
print('Введите координаты второго вектора')
x2, y2 = map(float, input().split())
if x1 * x2 + y1 * y2 == 0:
    print('Вектора перпендикулярны')
else:
    print('Вектора парралельны')