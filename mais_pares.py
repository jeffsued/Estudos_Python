def mais_pares(numero):
    pares = 0
    while True:
        if numero.isnumeric():
            int(numero) % 2 == 0
            pares += 1
        else:
            break
    return pares

def main():
    numero = ''
    while numero != 'fim':
        numero = input()
    else:
        print('elsedowhile')
    print(mais_pares(numero))

main()