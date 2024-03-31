print('-='*23)
print('{:^46}'.format('NOTAS - ANALISANDO E GERANDO DICIONÁRIOS 3'))
print('-='*23)
def notas(*n, sit=False):
    """
    -> Função para analisar notas e situação de vários alunos
    :param n:Uma ou mais notas dos aluno(s)
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    r=dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n)/len(n)
    media = sum(n)/len(n)


    if sit:
        if media >= 7:
            r['Situação'] = 'Boa'
        elif media < 5:
            r['Situação'] = 'Ruim'
        else:
            r['Situação'] = 'Razoável'

    return r


resp = notas(8,6,7,7,8.9,0,3, sit=True)
print(resp)
print('-='*23)
