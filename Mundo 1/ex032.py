from datetime import date

ano = int(input('Que ano quer analisar? Digite 0 para ano atual: '))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print('O ano {} é BISSEXTO'.format(ano))
        else:
            print('O ano {} NAO é BISSEXTO'.format(ano))            
    else:
        print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NAO é BISSEXTO'.format(ano))