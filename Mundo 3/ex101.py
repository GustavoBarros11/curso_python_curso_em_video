from datetime import date

def voto(idade):
    if idade >= 18 and idade <= 65:
        return 'VOTO OBRIGATÓRIO'
    elif (idade >= 16 and idade < 18) or idade > 65:
        return 'VOTO OPCIONAL'
    elif idade < 16:
        return 'NÃO VOTA'


print('-'*30)
ano_nasc = int(input('Em que ano você nasceu? '))
ano_atual = date.today().year

idade = ano_atual-ano_nasc
print(f'Com {idade} anos: {voto(idade)}!')