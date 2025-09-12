frase = input()
letra = input()

for i in letra:
    cont= 0
    for j in frase:
        if j == i:
            cont+=1
    print(i, cont) 