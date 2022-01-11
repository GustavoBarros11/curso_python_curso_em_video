nome = input('Digite o seu nome completo: ').strip()

primeiro_nome = nome.split()[0]
tot_letras = len(nome) - nome.count(' ')

print('Analisando o seu nome...')
print('Seu nome em maiusculas é', nome.upper())
print('Seu nome em minusculas é', nome.lower())
print('Seu nome tem ao todo {} letras'.format(tot_letras))
print('Seu primeiro nome é {} e ele tem {} letras'.format(primeiro_nome, len(primeiro_nome)))
