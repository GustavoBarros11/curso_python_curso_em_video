frase = str(input('Digite uma frase: ')).replace(' ', '')
contrario = frase[::-1]

print('O inverso de {} é {}'.format(frase, contrario))
if frase == contrario:
    print('Temos um palíndromo!')
else:
    print('Não temos um palíndromo!')
