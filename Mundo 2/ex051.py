print('='*35)
print('10 TERMOS DE UMA P.A.')
print('='*35)

ptermo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

for i in range(1, 11):
    print('{}'.format(ptermo + (i-1)*razao), end=' -> ')
print('ACABOU')