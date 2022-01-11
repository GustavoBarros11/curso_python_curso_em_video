# Input dos valores pelo usuário
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

# Operacoes Aritméticas
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
exp = n1**n2

# Imprime resultados na tela
print('A soma é {}, o produto é {} e a divisao é {:.2f}'.format(s, m, d))
print('A divisao inteira é {} e potencia é {}'.format(di, exp))