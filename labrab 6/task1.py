# Завдання 1. Дано n дійсних чисел:x1, x2, ..., xn. Знайти найменше серед додатніх.

n = int(input('Количество цифр: '))
list1 = [float(input('Введите эти цифры: ')) for x in range(n)]
list2 = [x for x in list1 if x > 0]

print(f'{min(list2)}')
