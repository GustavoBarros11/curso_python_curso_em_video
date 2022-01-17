lista = list()

for i in range(0, 5):
    num = int(input(f'Digite um numero para a Posicao {i}: '))
    lista.append(num)

maior = max(lista)
menor = min(lista)
pos_max = [pos for pos, num in enumerate(lista) if num == maior]
pos_min = [pos for pos, num in enumerate(lista) if num == menor]

print('=-'*25)
print('Voce digitou os valores', lista)
print(f'O maior valor digitado foi {maior} nas posicoes ', end='')
for pos in pos_max:
    print(f'{pos}...', end='')
print(f'\nO menor valor digitado foi {menor} nas posicoes ', end='')
for pos in pos_min:
    print(f'{pos}...', end='')
print()
