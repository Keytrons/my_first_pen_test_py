# №1
# Клиент приходит в кондитерскую. Он хочет приобрести один
# или несколько видов продукции, а также узнать её состав.
# Реализуйте кондитерскую. У вас есть словарь, где ключ –
# название продукции (торт, пирожное, маффин и т.д.).
# Значение – список, который содержит состав, цену (за 100гр)
# и кол-во (в граммах). Предложите выбор: 1. Если человек
# хочет посмотреть описание: название – описание 2.
# Если человек хочет посмотреть цену: название – цена.
# 3. Если человек хочет посмотреть количество: название – количество.
# 4. Всю информацию. 5. Приступить к покупке: С клавиатуры вводите
# название торта и его кол-во. n – выход из программы.
# Посчитать цену выбранных товаров и сколько товаров осталось в
# изначальном списке 6. До свидания.

products = {'Медовик': ['мука, сливочное масло, яйца, сахар, мёд, сода‚ '
                        'уксус, сметана, сливки, сахарная пудра.', 3.0, 8000],
            'Ореховый тарт': ['масло сливочное, сахарная пудра, сахар, сливки 33%, орех макадамия, '
                              'фундук очищенный, яйца, мука.', 7.9, 5000],
            'Пекановый пирог': ['мука, масло сливочное, яйца, соль, орех пекан, ванильный сахар, '
                                'молоко, тростниковый сахар, джем абрикосовый, коньяк.', 6.0, 10600],
            'Профитроли': [' мука, слив. масло, молоко, яйца, крем-чиз, сливки, сахарная пудра,'
                           ' желатин, ванилин, сахар, шоколад 68%, вода.', 8.1, 3030],
            'Тирамису': ['яйца, печенье Савоярди, сыр маскарпоне, лимонный сок, сахар, кофе '
                         'растворимый, какао, ром.', 5.8, 1500],
            'Печенье': [' овсяные хлопья, сливочное масло, сахар, яйца, мука, '
                        'шоколад 68%, шоколад термостабильный, сода, уксус, разрыхлитель.', 4.3, 5800]
            }
i = 0
print('В наличи имеется :')
for key in products:
    i += 1
    print(f' {i}) "{key}" ')
while True:
    enti = int(input('Введите цифру для просмотра : 1 - описания, 2 - цены (р), 3 - количества (гр.),'
                     ' 4 - всю информацию, 5 - приступить к покупке или 6 - До свидания! : '))
    if enti == 1:
        for k, v in products.items():
            print(f'Описание: "{k}" - {v[0]}')
    elif enti == 2:
        for k, v in products.items():
            print(f'Цена "{k}" - за 100 гр. {v[1]} руб.')
    elif enti == 3:
        for k, v in products.items():
            print(f'"{k}" - в наличии : {v[2]} грамм')
    elif enti == 4:
        for k, v in products.items():
            print(f'"{k}" - Состав : {v[0]} ;цена за 100 гр. {v[1]} руб. ; в наличии : {v[2]} грамм.')
    elif enti == 6:
        print('До свидания!')
        break
    elif enti == 5:
        suma = 0
        while True:
            ent = input('Введите товар который хотите приобрести или n для выхода : ')
            if ent == 'n':
                print(f'Сумма к оплате - {suma} руб.')
                input('***Оплатить***')
                break
            elif ent not in products:
                print('\n*Проверьте правильность ввода товара !*')
                break
            sgr = 0

            igr = products[ent][2]
            st = products[ent][1]
            hau = int(input(f'В наличии : {products[ent][2]} грамм. Сколько желаете ? - '))
            if hau <= igr:
                sgr += (hau / 100) * st
                raz = igr - hau
                products[ent][2] = raz
                print(f'Стоимость выбранного товара - {sgr} руб.')
                print(f'Осталось :')
                for k, v in products.items():
                    print(f'"{k}" - {v[2]} гр.')
            else:
                print('Столько нет ! Повторите запрос заново. ')
            suma += sgr
            print(f'Общая сумма - {suma} руб.')
    else:
        print('Введите правильную цифру !')
