num = int(input())
lista = input().split()

afirmativa = 'não'

for i in lista:
    if int(i) == num:
        afirmativa = 'sim'

print(afirmativa)