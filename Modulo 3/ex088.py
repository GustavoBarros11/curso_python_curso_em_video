from random import randint
from time import sleep

print('-'*40)
print('{:^40}'.format('JOGA NA MEGA SENA'))
print('-'*40)
tot_sorteos = int(input('Quantos jogos você quer que eu sorteie? '))

print(f'-=-=-= SORTEANDO {tot_sorteos} JOGOS -=-=-=')
for jogo in range(0, tot_sorteos):
    lista = []
    for c in range(0, 6):
        lista.append(randint(1, 60))
    print(f'Jogo {jogo+1}: {lista}')
    sleep(1)
    lista.clear()
print('-=-=-=-=-=-= < BOA SORTE > -=-=-=-=-=-=')
