def notas(*n, sit=False):
    """
        -> Função para analisar notas e situações de vários alunos.
        :param n: uma ou mais notas dos alunos (aceita várias)
        :param sit: valor opcional, indicando se deve ou não adicionar a situação
        :return: dicionário com várias informações sobre a situação da turma.
    """
    situacao = ''
    total = len(n)
    maior = max(n)
    menor = min(n)
    media = sum(n)/total
    resp = {'total': total, 'maior': maior, 'menor': menor, 'média': media}
    if sit:
        if media > 7:
            situacao = 'BOA'
        elif media > 5 and media < 7:
            situacao = 'RAZOÁVEL'
        else:
            situacao = 'RUIM'
        resp['situacao'] = situacao
    
    return resp
    

# resp = notas(5.5, 9.5, 10, 6.5)
resp = notas(3.5, 2, 6.5, 2, 7, 4, sit=True)
print(resp)
# help(notas)
