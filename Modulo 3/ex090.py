nome = str(input('Nome: '))
media = float(input('Média: '))
situacao = ''
if media < 7 and media >= 5:
    situacao = 'Recuperação'
elif media < 5:
    situacao = 'Reprovado'
else:
    situacao = 'Aprovado'

aluno = {"nome": nome, "media": media, "situacao": situacao}

print('-='*30)
print(f'  - nome é igual a {aluno["nome"]}.')
print(f'  - média é igual a {aluno["media"]:.1f}.')
print(f'  - situação é igual a {aluno["situacao"]}.')