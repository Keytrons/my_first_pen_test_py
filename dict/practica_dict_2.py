# Задача№2
# Дан словарь с числовыми значениями. Необходимо их все перемножить и вывести на экран.
cars = {'BMW 4 series Cbrio': 54,
        'BMW X6 M Competition': 260,
        'BMW 8 Gran Coupe': 110,
        'Tesla Model 3': 68,
        'Tesla Model S': 129,
        'Tesla Model X': 132
        }
summa = 1
for v in cars.values():
    summa *= v
print(f'Произведение стоимости всех авто : {summa} $')
