def insertion_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j+1], lista[j] = lista[j], lista[j+1]
    return lista

def main():
    lista = [5, 2, 20, 70, 1, 3, 7]
    ordenada = insertion_sort(lista)
    print(ordenada)
main()