a = [2, 3, 4, 7]
# Criar uma referencia em b para o mesmo espaco de memória representado pela variável a.
b = a
b[2] = 9
print(f'Lista A: {a}')
print(f'Lista B: {b}')

print('='*21)

c = [2, 3, 4, 7]
# Faz uma cópia dos elementos(não da referência), consequentemente eliminando o link entre as duas variáveis.
d = a[:]
d[2] = 9
print(f'Lista C: {c}')
print(f'Lista D: {d}')