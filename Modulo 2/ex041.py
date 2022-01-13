ano_nasc = int(input('Seu ano de nascimento: '))
ano_atual = 2017
idade = ano_atual-ano_nasc

print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFATIL')
elif idade <= 19:
    print('Classificação: JÚNIOR')
elif idade <= 25:
    print('Classificação: SENIOR')
else:
    print('Classificação: \033[1;32mMASTER\033[m')
