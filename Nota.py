print('-='*23)
print('{:^46}'.format('NOTAS - ANALISANDO E GERANDO DICIONÁRIOS'))
print('-='*23)
def notas(* nota, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param nota: uma ou mais notas dos alunos (aceita mais de uma).
    :param sit: parametro opcional. Se for True, retorna também a situação do aluno de acordo com a média.
    :return: dicionário com várias informações sobre a situação dos alunos.
    """
    dic = {'total': len(nota), 'media': sum(nota) / len(nota), 'menor': min(nota), 'maior': max(nota)}
    if sit:
        if dic['media'] < 6:
            dic['situação'] = 'RUIM'
        elif dic['media'] >= 7:
            dic['situação'] = 'BOA'
        else:
            dic['situação'] = 'RAZOÁVEL'
    return dic


resp = notas(5.5, 2.5, 1.5, 8, 3.5, 10, 9, 10, sit=True)
print(resp)
print('-='*23)