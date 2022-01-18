n = int(input('Введіть значення n:'))
a = [-4, 3]
new = []
sum = 0
b = int(input('Введіть значеня b:'))
c = int(input('Введіть значення c: '))
for i in range(2, n+1):
    newA = a[i-1]**2 + 2 * a[i-2] - i
    a.append(newA)

for el in a:
    if b < el <= c:
        sum += el
        new.append(el)
average = sum / len(new)
print(average)
