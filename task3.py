import os
os.system('cls')

a = input('Введите предложене - ')

os.system('cls')

b = a.split()
print('В вашем предложении ' + str(len(b)) + ' слов.')
b.sort()
print('Ваше предложение отсортировано в алфавитном порядке - ' + str(b))
print('Первая буква каждого слова вашего предложения заглавная - ' + str(a.title()))