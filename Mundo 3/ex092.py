from datetime import datetime

nome = str(input('Nome: '))
ano_nasc = int(input('Ano de Nascimento: '))
ano_atual = datetime.now().year
cart_trabson = int(input('Carteira de Trabalho (0 não tem): '))
dados = {"nome": nome, "ano_nasc": ano_nasc, "idade": (ano_atual-ano_nasc), "ctps": cart_trabson}

if cart_trabson != 0:
    dados["ano_contratacao"] = int(input('Ano de Contratação: '))
    dados["salario"] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['ano_contratacao']+35) - ano_atual)

print('-='*30)
print('  - nome tem o valor {}'.format(dados['nome']))
print('  - idade tem o valor {}'.format(dados['idade']))
print('  - ctps tem o valor {}'.format(dados['ctps']))
if cart_trabson != 0:
    print('  - contratação tem o valor {}'.format(dados['ano_contratacao']))
    print('  - salário tem o valor R${:.2f}'.format(dados['salario']))
    print('  - aposentadoria tem o valor {}'.format(dados['aposentadoria']))
