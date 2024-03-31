print('-='*23)
print('{:^46}'.format(' PROGRAMA DE VOTAÇÃO '))
print('-='*23)
def voto(ano):
    from datetime import date
    AnoAtual = date.today().year 
    idade = AnoAtual - nascimento
    if idade < 16:
        return f'COM {idade} anos: NÃO VOTA'
    elif 16 <= idade < 18:
        return f'COM {idade} anos: VOTO NÃO OBRIGATÓRIO'
    elif idade >= 18:
        return f'COM {idade} anos: VOTO OBRIGATÓRIO'
    else:
        return f'COM {idade} anos. VOTO OPCIONAL'
    
#PROGRAMA PRINCIPAL
nascimento = int(input('Informe sua data de nascimento: '))
print('')
print('-='*6,' RESULTADO DA CONSULTA ','-='*6)
print(voto(nascimento))   
print('-='*23)
 
