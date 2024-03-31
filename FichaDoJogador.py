print('-='*23)
print('{:^46}'.format('FICHA DO JOGADOR'))
print('-='*23)
def ficha(n, g):
    if n == '':
        n = '<desconhecido>'
    if g == '' or not g.isnumeric():
        g = '<não informado>'
    print(f'O jogador {n} fez {g} gol(s) no campeonato.')


# Programa Principal
n = str(input('Nome do Jogador: '))
g = input('N° Gols: ')
ficha(n, g)
print('-='*23)



