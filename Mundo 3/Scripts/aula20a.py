def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


# Empacotador (empacotamento)
def contador(*nums):
    # print(type(nums))
    # print(nums)
    tam = len(nums)
    print(f'Recebi os valores {nums} e são ao todo {tam} números.')


if __name__ == '__main__':
    soma(4, 5)
    print('-'*30)
    soma(b=4, a=5)

    # Função que recebe quantidade de parâmetros variável
    contador(2, 1, 7)
    contador(8, 8)
    contador(4, 4, 7, 6, 2)