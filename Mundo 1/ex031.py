dist = float(input('Qual a distancia da sua viagem? (km) '))

print('Voce esta prestes a começar uma viagem de {:.1f}km.'.format(dist))

if dist <= 200:
    preco = dist * 0.5
else:
    preco = dist * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preco))