ficha = list()

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))

    opcao = str(input('Quer continuar? [S/N] ')).strip().upper()
    if opcao != 'N' and opcao != 'S':
        print('Opção inválida. Saindo...')
    else:
        ficha.append([nome, nota1, nota2])
        if opcao == 'N':
            break

print('-='*35)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*25)
for i, gabarito in enumerate(ficha):
    print('{:<4}{:<10}{:>8.1f}'.format(i, gabarito[0], (gabarito[1]+gabarito[2])/2))
print('-'*30)
while True:
    n_aluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if n_aluno == 999:
        print('Finalizando...')
        break
    if n_aluno >= 0 and n_aluno < len(ficha):
        notas_aluno = ficha[n_aluno][1:]
        print(f'Notas de {ficha[n_aluno][0]} são {notas_aluno}')
    else:
        print('Opção inválida. Tente novamente...')
print('-'*30)
