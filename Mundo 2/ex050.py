quant = 0
soma = 0

for i in range(1, 7):
    valor = int(input('Digite o {} valor: '.format(i)))
    if valor % 2 == 0:
        quant += 1
        soma += valor
    
print('Você informou {} valores PARES e a soma foi {}'.format(quant, soma))
