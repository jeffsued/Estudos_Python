def encontros_vogais(palavra):
    vogais = 'aeiouAEIOU'
    for i in range(len(palavra)-1):
        if palavra[i] in vogais and palavra[i+1] in vogais:
            return True
    return False

def main():
    com = 0

    quantidade_de_palavras = int(input())
    palavras = []
    for i in range(quantidade_de_palavras):
        palavras.append(input())

    for palavra in palavras:
        if encontros_vogais(palavra):
            com += 1
    
    print('com:', com)
    print('sem:', quantidade_de_palavras - com)

main()