def dobra(lst):
    cont = 0
    while cont < len(lst):
        lst[cont] *= 2
        cont += 1


valores = [6, 3, 9, 1, 0, 2]
print('Lista Inicial: ', end='')
print(valores)

print('Lista Final: ', end='')
dobra(valores)
print(valores)
