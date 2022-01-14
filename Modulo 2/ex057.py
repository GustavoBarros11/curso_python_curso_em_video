sexo = ''

while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite o seu sexo [M/F]: ')).strip().upper()
    if sexo != 'M' and sexo != 'F':
        print('Por favor insira um valor válido como indicado entre colchetes [M/F]!')
    else:
        print('Obigado!')