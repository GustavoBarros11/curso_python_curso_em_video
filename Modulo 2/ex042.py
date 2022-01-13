p1 = int(input('Primeiro Segmento: '))
p2 = int(input('Segundo Segmento: '))
p3 = int(input('Terceiro Segmento: '))

if (p1+p2) > p3 and (p1+p3) > p2 and (p3+p2) > p1:
    print('Os segmentos acima PODEM FORMAR um triângulo', end=' ')
    if p1==p2 and p2==p3:
        print('EQUILÁTERO')
    elif (p1==p2 and p1!=p3) or (p2==p3 and p2!=p1) or (p1==p3 and p1!=p2):
        print('ISÓSCELES')
    else:
        print('ESCALENO')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo.')
    