def leiaInt(txt):
    while True:    
        try:
            n = int(input(txt))
        except ValueError:
            print('\033[1;31mERRO! Por favor, digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\033[1;31mUsuário preferiu não digitar esse numero.\033[m')
            
            return 0
        else:
            break        
    return n


def leiaFloat(txt):
    while True:    
        try:
            n = float(input(txt))
        except ValueError:
            print('\033[1;31mERRO! Por favor, digite um número real válido.\033[m')
        except KeyboardInterrupt:
            print('\033[1;31mUsuário preferiu não digitar esse numero.\033[m')
            
            return 0
        else:
            break
        
    return n


n = leiaInt('Digite um numero Inteiro: ')
x = leiaFloat('Digite um numero Real: ')
print(f'O valor inteiro digitado foi {n} e o real foi {x}')
