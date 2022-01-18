num = int(input('Digite um numero para ver sua tabuada: '))

print('-'*13)
for i in range(1 , 11):
    print('{} * {:2} = {:3}'.format(num, i, num*i))
print('-'*13)