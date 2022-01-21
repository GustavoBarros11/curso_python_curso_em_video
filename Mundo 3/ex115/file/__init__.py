import dado

# Acessar arquivo e mostrar lista de pessoas cadastradas
def mostrarCadastrados():
    dado.titulo('PESSOAS CADASTRADAS')
    try:
        print('Entrou 3')
        with open('ex115/data.txt', 'r+') as file:
            print(type(file))
            #i = 1
            #for line in file:
            #    dados = line.strip().split(",")
            #    print(f'  [{i}] {dados[0]:<24} {dados[1]} anos')
            #    i += 1
    except Exception as error:
       print(f'O erro foi {error.__cause__}')
       print('Alguma coisa')