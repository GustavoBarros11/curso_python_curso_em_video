print('-'*30)
print('Sequencia de Fibonacci')
print('-'*30)

ntermos = int(input('Quantos termos voce quer mostrar? '))
n1 = 0
n2 = 1

print('~'*30)
contador = 0
while ntermos > contador:
    if contador == 0:
        print(n1, end=' -> ')
    elif contador == 1:
        print(n2, end=' -> ')
    else:
        soma = n1+ n2
        n1 = n2
        n2 = soma
        print(soma, end=' -> ')
    contador += 1
print('FIM')
print('~'*30)