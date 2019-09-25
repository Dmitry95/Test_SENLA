import os
os.system('cls')

a = input('Введите текст - ')
b = input('Введите слово - ')

c = a.lower()
d = b.lower()

c = (c.casefold())
d = (d.casefold())

os.system('cls')

print( 'В ведённом вами тексте ' + str(c.count(d)) + ' раза встречается слово - ' + b )

