print('-='*23)
print('{:^46}'.format('NOTAS - ANALISANDO E GERANDO DICIONÁRIOS 2'))
print('-='*23)
def notas(* nota, sit=False):
    """
    -> Função para analísar notas e situação de vários alunos.
    param nota: uma ou mais notas dos alunos (aceita várias)
    param sit: valor opcional, indicando se deve ou não adicionar a situação
    return: dicionário com várias informações sonbre a situação da turma
    """
    boletim = dict()
    total = len(nota)
    soma = 0
    for i in range(len(nota)):
        if i == 0:
            maior_nota = nota[i]
            menor_nota = nota[i]
        if nota[i] > maior_nota:
            maior_nota = nota[i]
        else:
            if (nota[i] < menor_nota):
                menor_nota = nota[i]
        soma += nota[i]
    media = soma / total
    boletim['total'] = total
    boletim['maior'] = maior_nota
    boletim['menor'] = menor_nota
    boletim['média'] = media
    if (sit == True):
        if (media < 5):
            boletim['situação'] = 'RUIM'
        elif (media >= 5) and (media < 7):
            boletim['situação'] = 'RAZOÁVEL'
        else:
            if (media >= 7) and (media <= 10):
                boletim['situação'] = 'Boa'
    return(boletim)

# Programa principal
resp = notas(6.5, 8.2, 6.5, sit=True)
print(resp)
help(notas)
print('-='*23)
