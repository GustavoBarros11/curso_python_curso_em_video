num = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão:')
print('[ 1 ] BINÁRIO')
print('[ 2 ] OCTAL')
print('[ 3 ] HEXADECIMAL')
opcao = int(input('Sua opção: '))

if opcao == 1:
    print('O número {} em BINÁRIO corresponde a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('O número {} em OCTAL corresponde a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('O número {} em HEXADECIMAL corresponde a {}'.format(num, hex(num)[2:]))
else:
    print('Opção Inválida!')