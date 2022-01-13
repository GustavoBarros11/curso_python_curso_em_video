from random import randint
import random
from time import sleep

print("""SUAS OPÇÕES
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
""")
jogadas = ['PEDRA', 'PAPEL', 'TESOURA']
jogador = int(input('Qual é a sua jogada: '))
computador = random.randint(0, 2)

if jogador >= 0 and jogador < 3:
    sleep(0.75)
    print('JO')
    sleep(0.75)
    print('KEN')
    sleep(0.75)
    print('PO!!!')

    print("-="*11)
    print('Computador jogou', jogadas[computador])
    print('Jogador jogou', jogadas[jogador])
    print("-="*11)

    if jogador == computador:
        print('HOUVE EMPATE!!!')-2
        
    else:
        if jogador == 0 and computador == 1:
            print('COMPUTADOR VENCE')
        elif jogador == 0 and computador == 2:
            print('JOGADOR VENCE')
        elif jogador == 1 and computador == 0:
            print('JOGADOR VENCE')
        elif jogador == 1 and computador == 2:
            print('COMPUTADOR VENCE')
        elif jogador == 2 and computador == 0:
            print('COMPUTADOR VENCE')
        elif jogador == 2 and computador == 1:
            print('JOGADOR VENCE')
        else:
            print('Jogada inválida!')
else:
    print('Jogada inválida!')