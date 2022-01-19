from time import sleep

def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if inicio < fim:
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
        for i in range(inicio, fim+1, passo):
            sleep(0.25)
            print(f'{i}', end=' ')
        print('FIM!')
        print('-='*20)
    else:
        print(f'Contagem de {inicio} até {fim} de {abs(passo)} em {abs(passo)}')
        for i in range(inicio, fim-1, -abs(passo)):
            sleep(0.25)
            print(f'{i}', end=' ')
        print('FIM!')
        print('-='*20)


print('-='*20)
contador(1, 10, 1)
contador(10, 0, 2)    
print('Agora é a sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
