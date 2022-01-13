ano_nasc = int(input('Ano de nascimento: '))

idade = 2022 - ano_nasc

if idade < 18:
    print('Você ainda vai se alistar ao Serviço Militar')
    print('Precisamente daqui a {} anos ({}).'.format(18-idade, ano_nasc+18))
elif idade == 18:
    print('Você precisa se alistar este ano ao Serviço Militar')
else:
    print('Já passou o tempo do seu alistamento.')
    print('Precisamente {} anos desde {}, já que estamos em 2022.'.format(idade-18, ano_nasc+18))