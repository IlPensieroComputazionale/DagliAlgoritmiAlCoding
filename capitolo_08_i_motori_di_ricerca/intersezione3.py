# Programma INTERSEZIONE3 in Python
# Figura 8.7 del libro "Il Pensiero Computazionale: dagli algoritmi al coding"
# Autori: Paolo Ferragina e Fabrizio Luccio
# Edito da Il Mulino


def intersezione3(a, b):
    """
    Stampa tutti gli elementi del vettore a che sono contenuti anche nel vettore b.
    Entrambi i vettori devono essere ordinati.
    Piu' veloce di intersezione1 e intersezione2.
    :param a: vettore a di n elementi ordinato
    :param b: vettore b di m elementi ordinato
    """

    n = len(a)
    m = len(b)

    i = 0
    j = 0

    while (i < n) and (j < m):
        if a[i] < b[j]:
            i = i + 1
        elif b[j] < a[i]:
            j = j + 1
        else:
            print a[i]          # infatti a[i] = b[j]
            i = i + 1
            j = j + 1


def main():

    # entrambi i vettori sono ordinati
    pisa = [1, 3, 9, 144, 210]
    torre = [9, 11, 15, 21, 27, 89, 144, 150, 500, 800, 811]

    intersezione3(torre, pisa)


if __name__ == "__main__":
    main()
