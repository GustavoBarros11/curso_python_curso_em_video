n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
n3 = int(input('Digite mais um numero: '))
n4 = int(input('Digite o ultimo numero: '))

valores = (n1, n2, n3, n4)

print(f'Voce digitou os valores {valores}')
print(f'O valor 9 apareceu {valores.count(9) if 9 in valores else 0} vezes')
print(f'O valor 3 apareceu na {valores.index(3)+1 if 3 in valores else 0}* posicao')
print(f'Os valores pares digitados foram ', end=' ')
for valor in valores:
    if valor % 2 == 0:
        print(f'{valor}', end=' ')
print('')
