lista = [[], [], []]

for i in range(0, 3):
    for c in range(0, 3):
        lista[i].append(int(input(f'Digite um valor para [{i}, {c}]: ')))

print('-='*25)
for i in range(0, 3):
    for c in range(0, 3):
        print(f'[ {lista[i][c]:^3} ]', end='')
    print()