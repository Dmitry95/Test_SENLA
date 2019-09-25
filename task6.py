import os
os.system('cls')

W = []
P = []
K = int(input('Введите массу рюкзака - '))
n = int(input('Введите количество вещей - '))
k = K
Q = []
for q in range( int(n)):
    W.append(int(input('Введите массу - ')))
    P.append(int(input('Введите стоимость предметов - ')))
    
W = [0] + W
P = [0] + P
F = [ [0] * (K + 1) for i in range(n + 1)]
for i in range(1, n + 1):
    for k in range(1, K + 1):
        if k >= W[i]:
            F[i][k] = max(F[i - 1][k], F[i - 1][k - W[i]] + P[i]) 
        else: 
            F[i][k] = F[i - 1][k]
k = K
for i in range(n, 0, -1):
    if F[i][k] != F[i - 1][k]:
        Q.append(i) 
        k -= W[i]
Q.reverse()     
print('Предметы № ' + str(Q) + ' были добавлены в рюкзак!')