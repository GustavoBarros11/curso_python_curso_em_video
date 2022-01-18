lista = list()
pares = []
impares = []

while True:
    num = int(input('Digite um valor: '))
    lista.append(num)

    opcao = str(input('Quer continuar? [S/N] ')).strip().upper()
    if opcao != 'S' and opcao != 'N':
        print('Opcao inválida, VALOR DESCONSIDERADO! Tente outra vez...')
    else:
        if num % 2 == 1:
            impares.append(num)
        elif num % 2 == 0:
            pares.append(num)
        if opcao == 'N':
            break
                
print('-='*30)
print('A lista completa é', lista)
print('A lista de pares é', pares)
print('A lista de ímpares é', impares)
