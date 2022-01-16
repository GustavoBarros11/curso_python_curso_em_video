precos = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99,
'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.90)

print('-'*40)
print('{:^40}'.format('LISTAGEM DE PREÇOS'))
print('-'*40)

for i in range(0, len(precos), 2):
    print('{:.<30}R${:>7.2f}'.format(precos[i], precos[i+1]))
print('-'*40)
