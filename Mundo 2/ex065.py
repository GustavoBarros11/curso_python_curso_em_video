opcao = 'S'
maior = menor = totn = soma = 0

while opcao in 'S':
    numero = int(input('Digite um numero: '))
    opcao = str(input('Quer continuar? [S/N] ')).strip().upper()
    if not totn:
        menor = maior = numero
    else: 
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    totn += 1
    soma += numero
print('Voce digitou {} numeros e a média foi {:.2f}'.format(totn, soma/totn))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
