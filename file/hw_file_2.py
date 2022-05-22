# Домашнее задание
# Все операции выполнять с помощью встроенных функций библиотеки os
import fileinput
import os
# повторный запуск mkdir с тем же именем вызывает FileExistsError,
# вместо этого запустите:
if not os.path.isdir('C:/Users/user/Desktop/TXT'):
    os.mkdir('C:/Users/user/Desktop/TXT')  # Добавьте на свой рабочий стол папку,
os.chdir('C:/Users/user/Desktop/TXT')  # в ней создайте 3 текстовых файла:# test_1.txt, test_2.txt, test_3.txt.
with open('test_1.txt', 'w') as f:
    f.write('')
with open('test_2.txt', 'w') as f:
    f.write('')
with open('test_3.txt', 'w') as f:
    f.write('')
try:
    os.rename('test_1.txt', 'rename_1.txt')  # Затем переименуйте файлы на: rename_1.txt, rename_2.txt, rename_3.txt.
    os.rename('test_2.txt', 'rename_2.txt')
    os.rename('test_3.txt', 'rename_3.txt')
except FileExistsError:
    print('Ошибка в переименовании')
os.remove('rename_1.txt')
os.remove('rename_2.txt')
os.remove('rename_3.txt')
os.chdir('../../Prob')
os.rmdir('C:/Users/user/Desktop/TXT')  # После этого удалите созданную папку.
