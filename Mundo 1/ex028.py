import random
from time import sleep

print('-='*27)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar!')
print('-='*27)

numero_maquina = random.randint(0, 5)
numero = int(input('Em que numero eu pensei? '))

print('PROCESSANDO...')
sleep(1.5)

if numero == numero_maquina:
    print('PARABÉNS! Voce conseguiu me vencer.')
else:
    print('GANHEI! Eu pensei no numero {} e nao no {}!'.format(numero_maquina, numero))