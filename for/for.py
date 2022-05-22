c = input('Введите 3-х значное число *** :')
c = str(c)
for x in c :
    print(x)
c = int(c)
k = c % 10
m = c // 10
z = m % 10
v = m // 10
b = v + z + k
print(b)
