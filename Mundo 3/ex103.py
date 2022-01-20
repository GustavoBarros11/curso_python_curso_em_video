def ficha(nome='<desconhecido>', gols=0):
    if nome == '':
        nome = '<desconhecido>'
    print(f'O jogador {nome} fez {gols} gols(s) no campeonato.')


print('-'*30)
nome = str(input('Nome do jogador: '))
try:
    tot_gols = int(input('Total de gols: '))
except ValueError:
    tot_gols = 0
ficha(nome, tot_gols)