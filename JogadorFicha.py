print('-='*23)
print('{:^46}'.format('FICHA DO JOGADOR'))
print('-='*23)
def ficha(jogador=0, gols=0):
    if jogador == "":
        print(f"O jogador <desconhecido> fez {gols} gol(s) no campeonato.") #Ok, sem jogador somente o gol
    if jogador and gols:
        print(f"O jogador {jogador} fez {gols} gol(s) no campeonato.") #Ok, jogador e numero de gol
    if gols == False:
        print(f"O jogador {jogador} fez 0 gol(s) no campeonato.")


nome = str(input("Digite o nome do jogador: "))
gol = str(input("Digite o número de gol(s): "))
print('-='*23)
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
ficha(nome, gol)
print('-='*23)