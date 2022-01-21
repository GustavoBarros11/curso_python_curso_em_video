import dado
import file
if __name__ == '__main__':
    pare = False
    while not pare:
        dado.titulo('MENU PRINCIPAL', menu=True)
        opcao = 0
        while True:
            try:
                opcao = int(input('Sua opção: '))

                if opcao >= 1 and opcao <= 3:
                    break
                print('\033[0;37mPor favor, escolha uma das opções do MENU!\033[m')
            except ValueError:
                print('\033[0;31mERRO! Por favor, digite um numero inteiro válido.\033[m')
            except KeyboardInterrupt:
                print('\033[0;35m\nO usuário escolheu sair. Volte sempre!\033[m')
                pare = True
                break

        if opcao == 3:
            print('\033[0;35mSaindo do sistema... Até logo!\033[m')
            dado.printLinha()
            pare = True
            break
        elif opcao == 2:
            file.cadastrarPessoa()
        elif opcao == 1:
            file.mostrarCadastrados()