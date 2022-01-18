print('Gerador de PA')
print('-='*10)
pt = int(input('Primeiro termo: '))
razao = int(input('Razao da PA: '))
ntermos = 10
termo = 0

contador = ntermos
while contador > 0:
    termo = pt + (10-contador) * razao
    print('{}'.format(termo), end=' -> ')
    contador -= 1
print('Pausa', end='')


opcao = -1
while opcao != 0:
    opcao = int(input('\nQuantos termos voce quer mostrar a mais? '))
    
    if opcao != 0:
        amais = opcao
        ntermos += amais
        while amais > 0:
            termo = pt + (ntermos-amais) * razao
            print('{}'.format(termo), end=' -> ')
            amais -= 1
        print('Pausa', end='')
print('Progressao finalizada com {} termos mostrados.'.format(ntermos))