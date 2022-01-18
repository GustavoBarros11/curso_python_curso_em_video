num = int(input('Informe um numero: '))

print('Analisando o numero', num)
u = num // 1 % 10
d = num // 10 % 10 
c = num // 100 % 10
m = num // 1000 % 10

print('Unidade:', u)
print('Dezena:', d)
print('Centena:', c)
print('Milhar:', m)

#if len(num) == 1 and int(num) >= 0:
#    print('Unidade:', num[-1])
#    print('Dezena: 0')
#    print('Centena: 0')
#    print('Milhar: 0')
#elif len(num) == 2 and int(num) >= 0:
#    print('Unidade:', num[-1])
#    print('Dezena:', num[-2])
#    print('Centena: 0')
#    print('Milhar: 0')
#elif len(num) == 3 and int(num) >= 0:
#    print('Unidade:', num[-1])
#    print('Dezena:', num[-2])
#    print('Centena:', num[-3])
#    print('Milhar: 0')
#elif len(num) == 4 and int(num) >= 0:
#    print('Unidade:', num[-1])
#    print('Dezena:', num[-2])
#    print('Centena:', num[-3])
#    print('Milhar:', num[-4])
#else:
#    print('Insira um valor entre 0 e 9999')
