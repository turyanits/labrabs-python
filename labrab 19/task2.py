# Дано типізований файл, який містить деякий текст (кожен елемент типу string[40]). Вивести рядки тексту, які містять
# символ «А» у порядку зворотному до порядку слідування їх у файлі.
words = []
letter = 'A'
with open('txtfor2.txt', 'r') as file:
    for line in file:
        if letter in line:
            words.append(line)
words.reverse()
print(words)
