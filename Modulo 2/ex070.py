tot_gasto = tot_1000 = valor_barato = 0
nome_barato = ''

while True:
    print('-'*30)
    print('LOJA SUPER BARATAO')
    print('-'*30)

    opcao = ''
    nome = str(input('Nome do produto: '))
    valor = float(input('Preço: R$'))
    while opcao != 'S' and opcao != 'N':
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()

    if valor > 1000:
        tot_1000 += 1
    if tot_gasto == 0:
        valor_barato = valor
    if valor_barato > valor:
        valor_barato = valor
        nome_barato = nome
    tot_gasto += valor
    
    if opcao == 'N':
        break
print('------------------- FIM DO PROGRAMA -------------------')
print('O total da compra foi R${:.2f}'.format(tot_gasto))
print('Temos {} produtos custando mais de R$1000.00'.format(tot_1000))
print('O produto mais barato foi {} que custa R${:.2f}'.format(nome_barato, valor_barato))