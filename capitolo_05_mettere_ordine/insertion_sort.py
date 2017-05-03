# Programma INSERTION_SORT in Python
# Figura 5.2 del libro "Il Pensiero Computazionale: dagli algoritmi al coding"
# Autori: Paolo Ferragina e Fabrizio Luccio
# Edito da Il Mulino


def insertion_sort(c):
    """
    Ordina un vettore c di n elementi 
    tra i quali e' definita la relazione di confronto. 
    :param c: vettore da ordinare
    """

    n = len(c)                                  # n indica il numero di elementi di c

    for i in range(1, n):
        j = i
        while (j > 0) and (c[j - 1] > c[j]):
            tmp = c[j]                          # variabile temporanea per c[j]
            c[j] = c[j - 1]                     # scambia c[j-1] con c[j]
            c[j - 1] = tmp
            j = j - 1


def main():

    c = [3, 10, 13, 5, 2, 31, 4, 1, 6, 20, 16, 15, 12, 40, 50, 42]

    print c

    insertion_sort(c)

    print c


if __name__ == "__main__":
    main()