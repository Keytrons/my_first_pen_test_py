# Ввести в файл ‘input.txt’ 2 числа в одну строку через пробел.
# Вывести в файл ‘output.txt’ их разность
put=input('Введите 2 числа : ')
with open('input.txt','w') as f:#записали числа введенные с клавиатуры
    f.write(put)
# with open('input.txt') as f:
word = put
num =[int(w) for w in word.split() if w.isdigit()]#генератор списков
p=num[0]-num[1]
with open('output.txt','w') as f:
     f.write(str(p))
with open('output.txt') as f:
    print(f.readline())







