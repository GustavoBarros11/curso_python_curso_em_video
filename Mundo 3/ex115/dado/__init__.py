tam_linha = 40

def titulo(txt, menu=False):
    global tam_linha
    tam_linha = len(txt) + 4 if (len(txt) + 4) > tam_linha else tam_linha
    print('~'*tam_linha)
    print(txt.center(tam_linha))
    print('~'*tam_linha)
    if menu:
        print('\033[1;33m1\033[m - \033[0;36mVer pessoas cadastradas\033[m')
        print('\033[1;33m2\033[m - \033[0;36mCadastrar nova pessoa\033[m')
        print('\033[1;33m3\033[m - \033[0;36mSair do sistema\033[m')


def printLinha():
    print('~'*tam_linha)