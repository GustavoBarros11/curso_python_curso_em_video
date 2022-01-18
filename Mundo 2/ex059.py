from time import sleep

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))

opcao = 0

while opcao != 5:
    print("""    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR...
    """)

    opcao = int(input('>>>>> Qual é a sua opção? '))

    if opcao == 1:
        resultado = n1+n2
        print('A soma entre {} + {} é {}'.format(n1, n2, resultado))
    elif opcao == 2:
        resultado = n1*n2
        print('A multiplicação entre {} X {} é {}'.format(n1, n2, resultado))
    elif opcao == 3:
        resultado = max(n1, n2)
        print('Entre {} e {} o maior é {}'.format(n1, n2, resultado))
    elif opcao == 4:
        print('Informe os número novamente: ')
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo número: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente!')

    print('=-='*13)
    sleep(1)
print('Fim do programa! Volte sempre!')
