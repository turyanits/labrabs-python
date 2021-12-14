# Завдання 2. Дано три дійсних числа: a,b,c . Знайти min(a,b) + (min(b,c))**2.
a = float(input('a:'))
b = float(input('b:'))
c = float(input('c:'))
result = min(a, b) + (min(b, c))**2
print(result)