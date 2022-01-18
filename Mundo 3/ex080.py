lista_pre_ordenada = []

for i in range(0, 5):
    num = int(input('Digite um numero: '))
    if not len(lista_pre_ordenada):
        lista_pre_ordenada.append(num)
        print('Adicionado ao final da lista...')
    else:
        for c, valor in enumerate(lista_pre_ordenada):
            if num < valor:
                lista_pre_ordenada.insert(c, num)
                print('Adicionado na posicao {} da lista...'.format(c))
                break
            elif c == (len(lista_pre_ordenada)-1):
                lista_pre_ordenada.append(num)
                print('Adicionado ao final da lista...')
                break
print('-='*30)
print('Os valores digitados em orgem foram', lista_pre_ordenada)
