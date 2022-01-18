dias_al = int(input('Quantos dias alugados? '))
km_rodados = int(input('Quantos Km rodados? '))

preco = 60*dias_al + 0.15*km_rodados

print('O total a pagar é de R${:.2f} reais'.format(preco))