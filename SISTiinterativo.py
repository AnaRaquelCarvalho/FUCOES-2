print('-='*23)
print('{:^46}'.format('SISTEMA INTERATIVO DE AJUDA 2'))
print('-='*23)
from time import sleep
c = ('\033[m'               # 0 - SEM CORES
    '\033[0, 30, 41m'       # 1 - VERMELHO
    '\033[0, 30, 42m'       # 2 - VERDE
    '\033[0, 30, 43m'       # 3 - AMARELO      
    '\033[0, 30, 44m'       # 4 - AZUL
    '\033[0, 30, 45m'       # 5 - ROXO
    '\033[0, 30, 41m'       # 6 - BRANCO
    )
def ajuda(com):
    titulo(f'Acessando o Manual do comando \'{com}\'',4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~'* tam)
    print(f'{msg}')
    print('~'* tam)
    print(c[0], end='')
    sleep(1)

 #PROGRAMA PRINCIPAL
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PYHELP', 2)
    comando = str(input(" Função ou Biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!')               
print('-='*23)
    	