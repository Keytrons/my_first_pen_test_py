# 'ab'- сокращение от 'a'ddress'b'ook

ab = {'Swaroop':
          'swaroop@swaropch.com', 'Larry':
          'larry@wsll.org', 'Matsumoto':
          'matz@ruby-lang.org', 'Spammer':
          'spammer@hotmail.com'
      }
print("Адрес Swaroop'a:",ab['Swaroop'])

#Удаление пары ключ-значение
del ab['Spammer']
print('\nВ адресной книге {0} контакта\n'.format(len(ab)))

for name,addres in ab.items():
    print('Контакт {0} с адресом {1}'.format(name, addres))

#Добавление пары ключ-значение
ab['Guido']='guido@python.org'

if 'Guido' in ab:
    print()