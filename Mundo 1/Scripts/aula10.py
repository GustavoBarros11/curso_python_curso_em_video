nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))

media = (nota1+nota2) / 2

print('Sua média foi de {:.1f}'.format(media))
if media >= 6:
    print('Boa nota!')
else:
    print('Estude mais.')