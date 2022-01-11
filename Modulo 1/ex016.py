from math import trunc

valor = float(input('Digite um valor: '))
novo_valor = trunc(valor)

print('O valor digitado foi de {} e a sua porçao inteira é {}'.format(valor, novo_valor))