nome_hom_velho = ''
idade_hom_velho = 0
tot_idade = 0
tot_mul_menos_20 = 0

for i in range(0,4):
    print('----- {}° PESSOA -----'.format(i+1))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()

    tot_idade += idade
    if sexo == 'M':
        if idade > idade_hom_velho:
            nome_hom_velho = nome
            idade_hom_velho = idade
    else:
        if idade < 20:
            tot_mul_menos_20 += 1

media_idade_grupo = tot_idade / 4

print('A média de idade do grupo é de {:.1f} anos'.format(media_idade_grupo))
print('O homem mais velho tem {} anos e se chama {}.'.format(idade_hom_velho, nome_hom_velho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(tot_mul_menos_20))
        

