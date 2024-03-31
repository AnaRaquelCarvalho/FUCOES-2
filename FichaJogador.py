print('-='*23)
print('{:^46}'.format('FICHA DO JOGADOR 2'))
print('-='*23)
def ficha(jog = '<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')

#PROGRAMA PRINCIPAL
n = str(input('Nome do Jogador: '))
g = str(input('Número de Gol(s): '))
if g.isnumeric():
    g = int(g)
else:
    g = 0 
if n.strip()=='':
    ficha(gol=g)
else:
    ficha(n, g)  
print('-='*23)                     