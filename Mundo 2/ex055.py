maior = 0
menor = 0

for i in range(1, 6):
    peso = float(input('Peso da {}° pessoa: '.format(i)))

    if peso > maior:
        maior = peso
    if i == 1:
        menor = peso
    elif peso < menor:
        menor = peso

print('O maior peso lido foi de {:.1f}Kg'.format(maior))
print('O menor peso lido foi de {:.1f}Kg'.format(menor))
