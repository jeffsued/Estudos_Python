# unica entrada para dois jogadores
# contar quantas vezes cada jogador ganha e printar na saida
# condição de parada ambos colocarem 0 na entrada
j1 = 0
j2 = 0
while True:
    jogadores = input().split()
    jog1 = int(jogadores[0])
    jog2 = int(jogadores[1])
    if jog1 > jog2:
        j1 += 1
    elif jog2 > jog1:
        j2 += 1
    elif jog1 == 0 and jog2 == 0: 
        break
    else:
        j1 += 1
        j2 += 1

if j1 > j2:
    print('jogador 1 venceu')
elif j2 > j1:
    print('jogador 2 venceu')
else:
    print('empate')