# Словарь песен группы Depeche Mode
songsdict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 5.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}
# Выведите общее время звучания всех песен.
vals=[songsdict.values()]
s=[]
for i in vals:
    s+=i

print('Общее время звучания всех песен : ',sum(s),'минут ;')
# Создайте список песен, время звучания которых больше 5 минут
fay= {}
w=''
for fay,value in songsdict.items() :
    if value >= 5 :
        w+=fay
        if w!='':
            w+=' , '
print('Список песен, время звучания которых больше 5 минут : ',w.rstrip(' ,'))

# Создайте новый словарь тех песен, в название которых состоит из одного слова
i=[]
t=''
new=songsdict.copy()
kes=songsdict.keys()
for i in kes:
    if len(i.split(' '))>=2: #проверяем длинну слова, которые равны одному элемнту
        new.pop(i)
print('Словарь песен, название которых состоит из одного слова : ',new)


