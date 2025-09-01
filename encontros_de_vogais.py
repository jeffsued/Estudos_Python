def my_in(elem, sequencia):
    for i in sequencia:
        if i == elem:
            return True
    return False

def encontros_vogais(p):
    vogais = 'aeiouAEIOU'
    for i in range(len(p)-1):
        if my_in(p[i], vogais) and my_in(p[i+1], vogais):
            return True
    return False

def main():
    com = 0

    n = int(input())
    palavras = []
    for i in range(n):
        pal = input()
        palavras.append(pal)

    for p in palavras:
        if encontros_vogais(p):
            com += 1
    
    print('com:', com)
    print('sem:', n - com)

main()