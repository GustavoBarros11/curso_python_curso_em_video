nome_completo = input('Digite seu nome completo: ').strip()

nome_separado = nome_completo.split()

print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome_separado[0]))
print('Seu ultimo nome é {}'.format(nome_separado[-1]))