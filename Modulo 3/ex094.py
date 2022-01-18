pessoas =  []
tot_idade = 0
tot_m = 0

while True:
    pessoa = dict()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip()[0].upper()
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    if pessoa['sexo'] == 'F':
        tot_m += 1
    pessoa['idade'] = int(input('Idade: '))
    tot_idade += pessoa['idade']
    while True:
        opcao = str(input('Quer continar? [S/N] ')).strip()[0].upper()
        if temp_opcao in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N.')

    pessoas.append(pessoa.copy())
    pessoa.clear()
    if temp_opcao == 'N':
        break

print('-='*30)
print(f'A) Ao todos temos {len(pessoas)} pessoas cadastradas.')
print(f'B) A média de idade é de {(tot_idade)/len(pessoas):.2f} anos.')
print(f'C) As mulheres cadastradas foram {tot_m}:', end=' ')
for pessoa in pessoas:
    if pessoa['sexo'] == 'F':
        print(pessoa['nome'], end=' ')
print(f'\nD) Lista das pessoas que estão acima da média: ')
for pessoa in pessoas:
    if pessoa['idade'] > (tot_idade/len(pessoas)):
        for key, value in pessoa.items():
            print('    ', end='')
            print(f'{key} = {value};', end=' ')
        print()
