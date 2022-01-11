metros = float(input('Digite uma distancia em metros: '))

km = '{:.3f}km'.format(metros/1000)
hm = '{:.2f}hm'.format(metros/100)
dam = '{:.1f}dam'.format(metros/10)
dm = '{:.0f}dm'.format(metros*10)
cm = '{:.0f}cm'.format(metros*100)
mm = '{:.0f}mm'.format(metros*1000)

print('A medida de {:.1f}m corresponde a...'.format(metros))
print('{}\n{}\n{}\n{}\n{}\n{}'.format(km, hm, dam, dm, cm, mm))