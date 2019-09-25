import os
os.system('cls')

a = input('Введите целое число N - ')
os.system('cls')
while a.isdigit() != True:
    print('Вы ввели не целое число! А может быть и вовсе не число :)')
    a = input('Попробуйте еще раз - ')
    os.system('cls')

b = [i for i in range(0,int(a) + 1)]

d = [1,2,3,4,5,6,7,8,9,11,22,33,44,55,66,77,88,99]

c = list(set(b) & set(d))

c = sorted(c)

print('Полиндромы от 0 до ' + str(a) + ' это - ' + str(c))