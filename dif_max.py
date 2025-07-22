n = int(input())
seq = []

for i in range(n):
    seq.append(float(input()))

diferenca = 0
max1 = 0

for i in range(len(seq)- 1):
    dif = abs(seq[i] - seq[i+1])
    if dif > diferenca:
        diferenca = dif
        max1 = i

print(seq[max1], seq[max1+1])