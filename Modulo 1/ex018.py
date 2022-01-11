from math import sin, cos, tan, pi, radians

ang = int(input('Digite o angulo que voce deseja: '))

#sen = sin(ang*pi / 180)
sen = sin(radians(ang))
#cos = cos(ang*pi /180)
cos = cos(radians(ang))
#tg = tan(ang*pi /180)
tg = tan(radians(ang))

print('O angulo de {:.1f} graus tem o SENO de {:.2f}'.format(ang, sen))
print('O angulo de {:.1f} graus tem o COSSENO de {:.2f}'.format(ang, cos))
print('O angulo de {:.1f} graus tem a TANGENTE de {:.2f}'.format(ang, tg))
