lista = [[], [], []]
tot_val = sum_ter = 0

for i in range(0, 3):
    for c in range(0, 3):
        lista[i].append(int(input(f'Digite um valor para [{i}, {c}]: ')))

print('-='*25)
for i in range(0, 3):
    for c in range(0, 3):
        print(f'[ {lista[i][c]:^3} ]', end='')
        if lista[i][c] % 2 == 0:
            tot_val += lista[i][c]
        if c == 2:
            sum_ter += lista[i][c]
    print()
print('-='*25)
print(f'A soma dos valores pares é {tot_val}.')
print(f'A soma dos valores da terceira coluna é {sum_ter}.')
print(f'O maior valor da 2° linha é {max(lista[1])}.')