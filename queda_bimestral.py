meses = input().split(',')
bimestres = []

for i in range(0,12,2):
    
    media = ((int(meses[i]) + int(meses[i+1])) / 2)
    bimestres.append(media)
    print(f'{(i/2)+1:.0f} bimestre: {media:.1f}')

print('queda bimestral:')

queda = False

for medias in range(1,6):
    
    if bimestres[medias] < bimestres[medias - 1]:
        print(medias + 1)
        queda = True
if queda == False:
    print('nenhum')    
