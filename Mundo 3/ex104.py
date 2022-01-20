def leiaInt(txt):
    while True:    
        try:
            n = int(input(txt))

            if type(n) == int:
                break
        except ValueError:
            print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')
        
    return n

n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')