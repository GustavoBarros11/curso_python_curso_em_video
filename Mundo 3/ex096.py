def area(larg, alt):
    area = larg*alt
    print(f'A área de um terreno {larg:.1f}x{alt:.1f} é de {area:.1f}m².')


print(' Controle de Terrenos ')
print('-'*22)

largura = float(input('Largura (m): '))
altura = float(input('Comprimento (m): '))
area(largura, altura)