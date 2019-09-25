import os
os.system('cls')

a = input('Введите первое целое число - ')
b = input('Введите второе целое число - ')

while a.isdigit() != True or b.isdigit() != True:
    print('Вы ввели не целые числа или букву')
    a = input('Введите первое целое число - ')
    b = input('Введите второе целое число - ')

a = int(a)
b = int(b)
m = a * b

while a != 0 and b != 0:
    if a > b:
        a %= b
    else:
        b %= a
        
os.system('cls')

d = a + b
print('Наибольший общий делитель - ' + str(d))

k = m // d

print('Наибольшее общее кратное - ' + str(k))