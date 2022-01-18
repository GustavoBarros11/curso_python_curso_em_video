print('='*11, end=' ')
print('LOJAS GUANABARA', end=' ')
print('='*11)
preco = float(input('Preço das compras: R$'))

print("""FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
""")
opcao = int(input('Insira uma opção: '))

if opcao == 1:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, preco*0.9))
elif opcao == 2:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, preco*0.95))
elif opcao == 3:
    print('Sua compra será parcelada em 2x de R${} SEM JUROS\nCustando no total R${:.2f}'.format(preco/2, preco))
elif opcao == 4:
    nparcelas = int(input('Quantas parcelas: '))
    novo_preco = preco*1.2
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS\nSua compra de R${:.2f} vai custar R${:.2f} no final.'.format(nparcelas, novo_preco/nparcelas, preco, novo_preco))
else:
    print('Opção inválida.')

