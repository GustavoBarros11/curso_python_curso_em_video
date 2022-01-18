lista = list()

while True:
    num = int(input('Digite um valor: '))
    lista.append(num)

    opcao = str(input('Quer continuar? [S/N] ')).strip().upper()
    if opcao != 'S' and opcao != 'N':
        print('Opcao inválida! Tente outra vez...')
    else:
        if opcao == 'N':
            print('-='*30)
            print('Voce digitou {} elementos.'.format(len(lista)))
            print('Os valores em ordem crescente sao {}'.format(sorted(lista, reverse=True)))
            print('O valor 5 parte {}faz parte da lista!'.format('' if 5 in lista else 'não '))
            break