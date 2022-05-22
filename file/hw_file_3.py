# Задача№1

with open('txt.txt') as string:
    a = string.readlines()
    print('Количество строк :', len(a))  # В текстовом файле посчитать количество строк
    n = 0
    for i in a:  # для каждой отдельной строки определить количество в ней символов.
        i = i[:-1]
        n += 1
        el = len(i)
        print(f'{n}) {i} : {el}')
