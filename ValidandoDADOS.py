print('-='*23)
print('{:^46}'.format('VALIDANDO ENTRADA DE DADOS EM PYTHON'))
print('-='*23)
def leiaInt(a: str):
    while True:
        valor = input(a)
        if valor.isnumeric():
            return int(valor)
        else:
            print('\033[31mERRO! Digite um número válido\033[m')


n = leiaInt('Digite um valor: ')
print(f'Você acabou de digitar o número {n}')
print('-='*23)