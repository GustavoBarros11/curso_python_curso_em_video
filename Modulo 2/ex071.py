print('='*30)
print('{:^30}'.format('BANCO CSV'))
print('='*30)

tot50 = tot20 = tot10 = tot1 = 0

valor = int(input('Digite um valor: R$'))

tot50 = valor // 50
valor -= tot50*50
tot20 = valor // 20
valor -= tot20*20
tot10 = valor // 10
valor -= tot10*10
tot1 = valor

if tot50:
    print(f'Total de {tot50} cédulas de R$50')
if tot20:
    print(f'Total de {tot20} cédulas de R$20')
if tot10:
    print(f'Total de {tot10} cédulas de R$10')
if tot1:
    print(f'Total de {tot1} cédulas de R$1')
print('='*30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
