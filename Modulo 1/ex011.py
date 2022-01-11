largura = float(input('Largura da parede (metros): '))
altura = float(input('Altura da parede (metros): '))

area = altura*largura

print('Sua parede tem a dimensao de {:.2f}x{:.2f} e sua área é de {:.3f}m2.'.format(largura, altura, area))
print('Para pintar essa parede, voce precisará  de {:.5}l de tinta.'.format(area/2))