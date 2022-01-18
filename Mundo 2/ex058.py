import random
from time import sleep

print('-='*27)
print('Sou seu computador')
print('Vou pensar em um numero entre 0 e 10. Tente adivinhar!')
print('Será que você consegue adivinhar qual foi?')
print('-='*27)

numero_maquina = random.randint(0, 10)
palpite = -1
tentativas = 0

while palpite != numero_maquina:
    palpite = int(input('Qual é seu palpite? '))
    tentativas += 1
    if palpite < numero_maquina:
        print('\033[1;34mMais...\033[m Tente mais uma vez!')
    else:
        print('\033[1;33mMenos...\033[m Tente mais uma vez!')
print('Acertou com {} tentativas. \033[1;32mParabéns\033[m!!!'.format(tentativas))
