from random import randint
from time import sleep

numeros = []

def sorteia():
    print('Sorteando 5 valores da list: ', end='')
    for c in range(0, 5):
        sleep(0.4)
        numeros.append(randint(0, 10))
        print(f'{numeros[c]}', end=' ')
    print('PRONTO!')

    return numeros[:]
    

def somaPar(lst):
    sum = 0
    for num in lst:
        if num%2 == 0:
            sum += num
    return sum


sorteia()
print(f'Somando os valores pares de {numeros}, temos {somaPar(numeros)}')    
