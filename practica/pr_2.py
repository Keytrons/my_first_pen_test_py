# Посчитать, сколько раз встречается определенная цифра(цифра – это от 0 до 9) в списке чисел.
# Количество введенных чисел в список и искомая цифра задаются с клавиатуры.
# Числа выбираются рандомно.
kol_ch = int(input('Введите количество введеных чисел в список : '))
isk = int(input('Введите искомую цифру от 0-9 : '))
b = 0
import random
a = [random.randint(0, 9) for i in range(kol_ch)]
for i in a:
    if i == isk:
        b += 1
print(a)
print('Заданная цифра нашлась', b, 'раз')
