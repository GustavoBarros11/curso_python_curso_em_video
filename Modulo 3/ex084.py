lista_pessoas = []

while True:
    lista_pessoas.append(str(input('Nome: ')))
    lista_pessoas.append(float(input('Peso: ')))

    opcao = str(input('Quer continuar? [S/N] ')).strip().upper()
    if opcao != 'S' and opcao != 'N':
        print('Opção inválida! Continuando...')
    if opcao == 'N':
        break

tot_pessoas = int(len(lista_pessoas) / 2)
lista_pesos = [lista_pessoas[c] for c in range(1, len(lista_pessoas), 2)]
maior_nomes = [lista_pessoas[c-1] for c in range(1, len(lista_pessoas), 2) if lista_pessoas[c] == max(lista_pesos)]
menor_nomes = [lista_pessoas[c-1] for c in range(1, len(lista_pessoas), 2) if lista_pessoas[c] == min(lista_pesos)]
maior = max(lista_pesos)
menor = min(lista_pesos)

print(f'Ao todo você cadastrou {tot_pessoas} pessoas.')
print(f'O maior peso foi de {maior:.2f}kg. Peso de {maior_nomes}')
print(f'O menor peso foi de {menor:.2f}kg. Peso de {menor_nomes}')