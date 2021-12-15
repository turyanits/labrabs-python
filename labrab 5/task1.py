from math import cos
# Завдання 1. Дано натуральне число n і дійсне число x. Обчислити cos x + cos^2 x + ... cos^n x
n = int(input("input n:"))
x = float(input("Input X:"))
sum = 0
for i in range(1,n+1):
    sum += cos(x) **i
print(sum)
