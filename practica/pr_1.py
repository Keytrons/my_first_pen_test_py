# С клавиатуры вводится 7-значное число. Если четных цифр в нем больше,
# чем нечетных, то найти сумму всех его цифр, если нечетных больше,
# то найти произведение 1 3 и 6 цифры.
a = input('Введите 7-и значное число :')
b = 0
c = 0
e = 0
k = 0
for i in a:
    if int(i) % 2 == 0:
        b += 1
        e += int(i)
    else:
        c += 1
        k += int(i)
d=k+e
if b > c:
    print('Сумма всех цифр =',d )
elif b < c:
    z = int(a[0]) * int(a[2]) * int(a[5])
    print('Произведение 1,3 и 6 цифры =', z)
