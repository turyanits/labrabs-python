# Дано текстовий файл, який містить дійсні числа. Визначити найменший елемент серед додатніх.
numbers = []
with open('txtfor1.txt') as file:
    for line in file:
        number = float(line)
        if number > 0:
            numbers.append(num)
print(min(numbers))