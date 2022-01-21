import dado

# Acessar arquivo e mostrar lista de pessoas cadastradas
def mostrarCadastrados():
    dado.titulo('PESSOAS CADASTRADAS')
    try:
        with open('/home/gustavos/Scripts/python_course_cursoemvideo/Mundo 3/ex115/data.txt', 'r+') as file:
            i = 1
            for line in file:
                dados = line.strip().split(",")
                print(f'  [{i}] {dados[0]:<24} {dados[1]} anos')
                i += 1
    except Exception as error:
        print('Error')
       # try:
       #     with open('/home/gustavos/Scripts/python_course_cursoemvideo/Mundo 3/ex115/data.txt', 'w+') as file:
       #         file.write('')
       #         print('\033[0;34mZero usuários cadastrados.\033[m')
       # except Exception as error:
       #     print(f'\033[0;31mError! The error was {error.__class__}.\033[m')


def cadastrarPessoa():
    dado.titulo('NOVO CADASTRO')
    nome = str(input(('Nome: ')))

    while True:
        try:
            idade = int(input('Idade: '))

            if idade > 1:
                break
            print('\033[0;31mERRO: Por favor, digite uma idade válida!\033[m')
        except ValueError:
            print('\033[0;31mERRO: Por favor, digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\033[0;35m\nO usuário escolheu sair. Volte sempre!\033[m')
            break
    adicionarPessoaNoArquivo(nome, idade)

def adicionarPessoaNoArquivo(nome, idade):
    try:
        with open('/home/gustavos/Scripts/python_course_cursoemvideo/Mundo 3/ex115/data.txt', 'a+') as file:
            file.write(f'\n{nome},{idade}')
            print(f'\033[0;32mNovo registro de {nome} adicionado.\033[m')
    except Exception as e:
        print(f'\033[0;31mERRO: O erro foi {e.__class__}.\033[m')



