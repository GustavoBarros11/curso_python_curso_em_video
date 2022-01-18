from random import randint
from time import sleep

jogadas = {}

for i in range(1, 5):
    valor = randint(1, 6)
    jogadas[f'Jogador {i}'] = valor
    print(f'Jogador {i} tirou {valor} no dado.')
    sleep(0.5)

# for key, value in jogadas.items():
#     if key == 'Jogador 1':
#         ordenado.append(jogadas)
#     else:

ordernado = dict(sorted(jogadas.items(), key=lambda item: item[1], reverse=True))
print('-='*30)
print(f'{"== RANKING DOS JOGADORES ==":^30}')
pos = 0
for key, value in ordernado.items():
    pos += 1
    print(f'{pos:>3}° lugar: {key:>7} com {value}.')
    sleep(1)
