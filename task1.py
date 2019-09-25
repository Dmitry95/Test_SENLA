import os
os.system('cls')

import math

a = input('Введите целое число - ')

os.system('cls')

while a.isdigit() != True:
    print('Вы ввели не целое число! А может быть и вовсе не число :)')
    a = input('Попробуйте еще раз - ')
    os.system('cls')
b = ( int(a) % 2 )
a = int(a)
    
def numbers(a):
    i = 2
    limit = int(math.sqrt(a))
    while i <= limit:
        if a % i == 0:
            print("составное число!")
            quit()
        i += 1
    print("простое число!")
        
if (b == 1):
    print( str(a) + ' - Нечётное',end=' ')
    numbers(a)
elif (b == 0):
    print( str(a) + ' - Чётное',end=' ')
    numbers(a)
