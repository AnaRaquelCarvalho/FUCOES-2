print('-='*23)
print('{:^46}'.format('SISTEMA INTERATIVO DE AJUDA'))
print('-='*23)
from random import randint
from time import sleep
def linha(l):
    print('-' * 50)
    print(l.center(50))
    print('-' * 50)
def color(cor=2,fundo=0):
    for c in range(0,7):
        if cor == c:
            print(f'\033[1;3{c}m',end= '')
        if fundo == c:
            print(f'\033[1;4{c}m',end= '')
def manual(com):
    e1 = randint(0,7)
    e2 = randint(0,7)
    if e1 == e2 or e1 == 6 and e2 == 4 or e1 == 4 and e2 == 6:
        color(cor=2,fundo=0)
    else:
        color(cor=e1,fundo=e2)
    help(com)


color(cor=4,fundo=7)
linha('SISTEMA DE AJUDA PYHELP')
while True:
    color(cor=2,fundo=0)
    fun = input('Função ou Biblioteca: ')
    if fun.lower() == 'fim':
        break
    else:
        color(cor=4, fundo=7)
        linha(f'ACESSANDO COMANDO {fun.upper()}')
        sleep(1)
        manual(fun)
print('-='*23)        
