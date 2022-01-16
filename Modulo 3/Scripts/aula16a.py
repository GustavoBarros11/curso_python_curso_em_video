lanche = 'hamburguer'
# Tuplas sao imutaveis
lanches = 'Hamburguer', 'Suco', 'Pizza', 'Pudim'

print(lanches[1:3])

for comida in lanches:
    print(f'Eu vou comer {comida}')

for cont in range(0, len(lanches)):
    print(f'Eu vou comer {lanches[cont]} na posicao {cont}')

for pos, comida in enumerate(lanches):
    print(f'Eu vou comer {comida} na posicao {pos}')

print('Comi pra caramba!')