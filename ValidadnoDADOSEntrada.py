print('-='*23)
print('{:^46}'.format('VALIDANDO ENTRADA DE DADOS EM PYTHON 3'))
print('-='*23)
def leiaint():
    n = str(input('Digite um número: '))
    while not n.isnumeric():
        print('\033[31mERRO! Digite um número válido\033[m')
        n = str(input('Digite um número: '))
    if n.isnumeric():
        n = int(n)
        print(f'Você digitou o número: {n} ')


leiaint()
print('-='*23)