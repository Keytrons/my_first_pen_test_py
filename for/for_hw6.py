#Задача №1 (решить через for)
#Выведи на экран все числа в диапазоне от 54 до 9184 кратные 5
for i in range(54,9184):
    if i%5 ==0: #Если число кратно 5
        print(i, '- это число кратно 5 ') #то, вывести его
