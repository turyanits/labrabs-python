# Завдання 4. Нехай  x_0 = 0, x_1 = 7, x_i = x_i(1+x_(i-2)), де i = 2,3,...
n = int(input('n:'))
a = 0
b = 7
c = 1
x = 0

while c < n:
    x = b * 2 + a
    a = b
    b = x
    c += 1
print('xn = {0}'.format(x))
