print('-='*23)
print('{:^46}'.format(' FATORIAL '))
print('-='*23)

def fatorial(n, show=False):
    """
    Função que calcula o fatorial de um número.
    :param n: número que terá seu fatorial calculado.
    :param show: bool opcional que definirá se o processo
    de calculo será ou não mostrado.
    :return: o resultado e o processo de calculo caso o valor
    de :param show: seja True.
    """
from random import randint
def fatorial(n,show=False):
    print(f'Valor sorteado: {n}')
    print(f'{n} x',end= " ")
    for v in range(n-1,0,-1):
        n *= v
        if show == True:
            print(v,"x " if v != 1  else "= ", end ="")
    print(n)
n = randint(2,7)
print('')
print('-='*4,'MOSTRAR COM CALCULO','-='*4)
fatorial(n,show=True)
print('')
print('-='*4,'MOSTRAR SEM CALCULO','-='*4)
fatorial(n,show=False)
print('-='*23)
