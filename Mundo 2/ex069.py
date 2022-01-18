mais18 = tot_h = tot_m_20 = 0

while True:
    print('-'*25)
    print('{}'.format('CADASTRE UMA PESSOA'))
    print('-'*25)
    idade = int(input('Idade: '))
    sexo = opcao = ''
    while sexo != 'F' and sexo != 'M':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()
    print('-'*25)
    while opcao != 'S' and opcao != 'N':
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()

    if idade > 18:
        mais18 += 1
    if 'M' in sexo:
        tot_h += 1
    if 'F' in sexo and idade < 20:
        tot_m_20 += 1
    if 'N' in opcao:
        break 
print('====== FIM DO PROGRAMA ======')
print(f'Total de pessoas com mais de 18 anos: {mais18}')
print(f'Ao todo temos {tot_h} homens cadastrados')
print(f'E temos {tot_m_20} mulheres com menos de 20 anos')
