lista = list()

while True:
    num = int(input('Digite um valor: '))
    if num in lista:
        print('Valor duplicado! Não vou adicionar...')
    else:
        lista.append(num)
        print('Valor adicionado com sucesso...')

    opcao = str(input('Quer continuar? [S/N] ')).strip().upper()
    if opcao != 'S' and opcao != 'N':
        print('Opcao inválida! Tente outra vez...')
    else:
        if opcao == 'N':
            print('-='*30)
            print('Voce digitou os valores', lista)
            break
