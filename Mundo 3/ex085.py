lista = [[], []]

for i in range(0, 7):
    num = int(input(f'Digite o {i+1}° valor: '))

    if int(str(num)[-1]) % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)

print('-='*24)
print(f'Os valores pares digitados foram:', sorted(lista[0]))
print(f'Os valores ímpares digitados foram:', sorted(lista[1]))