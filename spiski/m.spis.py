#Введи список, отсортируй его и оставь только уникальные элементы
#Примечание: Уникальные элементы - это элементы, которые появляются только один раз в списке
my_sp=[22,32,4,14,"Hello","world",20,22,4,32,14,'world']
h_sp=[]
for i in my_sp:
    if i not in h_sp:
        h_sp.append(i)
for i in h_sp:
    print(i,end =',')