from math import pow, hypot

cat_op = float(input('Comprimento do cateto oposto: '))
cat_ad = float(input('Comprimento do cateto adjacente: '))

#hipotenusa = pow(cat_op**2 + cat_ad**2, (1/2))
hipotenusa = hypot(cat_op, cat_ad)

print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))