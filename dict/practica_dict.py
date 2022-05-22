#Задача№1
#Значениями словаря могут быть и списки. Создайте словарь с ключами BMW,
# Tesla и списками из 3х моделей в качестве значений. Выведите первое и
# последнее значения каждого из ключей.
cars={'BMW':['4 series Cbrio','X6 M Competition','8 Gran Coupe'],
'Tesla':['Model 3','Model S','Model X']}
car=cars.copy()
#car=car.values()
for k, v in cars.items():
    print(f'Марка авто : {k} , модель : {v[0]},{v[2]}')