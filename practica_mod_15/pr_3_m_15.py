# В текстовый файл построчно записаны фамилия и имя учащихся класса
# и его оценка за контрольную. Вывести на экран всех учащихся, чья оценка
# меньше 3 баллов и посчитать средний балл по классу.
with open('class.txt', encoding='utf-8') as f:
    st = f.read()
st = st.split('\n')
print(st)
suma = 0
s = 0
for i in st:
    for j in i.split(" "):
        if j.isdigit():
            j = int(j)
            suma += j
            if j < 3:
                s += 1
                print(f'{s}) {i.split()[0]}')
sr = suma / len(st)
print(f'Средний бал по классу : {sr}')
