valor_casa = float(input('Insira o valor da casa: R$ '))
salario = float(input('Insira o seu salário: R$ '))
tot_anos_pagar = int(input('Total de anos para quitar a divida: '))

prest_mensal = valor_casa / (tot_anos_pagar*12)

if prest_mensal > (salario*0.3):
    print('Empréstimo \033[1;31mNEGADO\033[m! O valor da prestação excede o limite de 30% do seu salário :(')
    print('Valor da prestação: R${:.2f}'.format(prest_mensal))
else:
    print('Empréstimo \033[1;32mAprovado\033[m! :)')
    print('Valor da prestação: R${:.2f}'.format(prest_mensal))