ano_atual = 2017
tot_maior_idade = 0
tot_menor_idade = 0

for i in range(1, 8):
    ano_nasc = int(input('Em que ano a {}° pessoa nasceu? '.format(i)))
    if ano_atual - ano_nasc >= 18:
        tot_maior_idade += 1
    else:
        tot_menor_idade += 1

print('Ao todo tivemos {} pessoas maiores de idade'.format(tot_maior_idade))
print('E também tivemos {} pessoas menores de idade'.format(tot_menor_idade))