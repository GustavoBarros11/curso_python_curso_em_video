while True:
    print('\033[0;30;42m', end='')
    print('~'*(len('SISTEMA DE AJUDA PyHELP')+4))
    print('  SISTEMA DE AJUDA PyHELP  ')
    print('~'*(len('SISTEMA DE AJUDA PyHELP')+4), end='\033[m\n')
    nome = str(input('Função ou Biblioteca >> '))
    if nome in 'FIMfimFim':
        break
    print('\033[0;30;46m', end='')
    print('~'*(len(f'Acessando o Manual do Comando {nome}')+4))
    print(f'  Acessando o Manual do Comando {nome}  ')
    print('~'*(len(f'Acessando o Manual do Comando {nome}')+4), end='\033[m\n')
    print('\033[7m', end='')
    help(nome)
    print('\033[m', end='')
print('\033[0;30;41m', end='')
print('~'*(len(f'ATÉ LOGO!')+4))
print(f'  ATÉ LOGO!  ')
print('~'*(len(f'ATÉ LOGO!')+4), end='\033[m\n')