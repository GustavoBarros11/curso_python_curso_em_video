n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))

media = (n1+n2) / 2

print('Tirando {} e {}, a média do aluno é {:.1f}'.format(n1, n2, media))
if media < 5:
    print('Resultado: REPROVADO')
elif media >= 5 and media <= 6.9:
    print('Resultado: RECUPERAÇÃO')
else:
    print('Resultado: APROVADO')