while True:
    n = int(input('Quer ver a tabuada de qual valor? '))

    if n < 0:
        break
    else:
        print('-'*30)
        for i in range(1, 11):
            print(f'{i} x {n} = {i*n}')
        print('-'*30)
print('-'*30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')