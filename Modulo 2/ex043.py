from math import pow

peso = float(input('Qual é o seu peso: (kg) '))
altura = float(input('Qual á a sua altura: (m) '))

imc = peso / pow(altura, 2)

print('O IMC desta pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Situação: Abaixo do Peso')
elif imc >= 18.5 and imc < 25:
    print('Situação: Peso Ideal')
elif imc >= 25 and imc < 30:
    print('Situação: Sobrepeso')
elif imc >= 30 and imc < 40:
    print('Situação: Obesidade')
else:
    print('Situação: Obesidade Mórbida')