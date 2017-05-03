# Programma MERGE_SORT in Python
# Figura 5.6 del libro "Il Pensiero Computazionale: dagli algoritmi al coding"
# Autori: Paolo Ferragina e Fabrizio Luccio
# Edito da Il Mulino


# carica le funzioni matematiche
import math


def merge_sort(c):
    """
    Ordina un vettore c di n = 2^h interi tra i quali e' definita la relazione di confronto <=. 
    Utilizza al suo interno la struttura del programma fusione
    :param c: vettore da ordinare
    """

    n = len(c)                  # n indica il numero di elementi di c

    h = int(math.log(n, 2))

    f = [None] * n              # inizializza il vettore ausiliario f

    for r in range(1, h+1):
        for s in range(0, 2**(h-r)):
            a = 2**r * s
            b = a + 2**(r-1)
            i = a
            j = b
            k = a

            while (i < a + 2**(r-1)) and (j < b + 2**(r-1)):
                if c[i] <= c[j]:
                    f[k] = c[i]
                    i = i + 1
                else:
                    f[k] = c[j]
                    j = j + 1
                k = k + 1

            while (i < a + 2**(r-1)):
                f[k] = c[i]
                i = i + 1
                k = k + 1

            while (j < b + 2**(r-1)):
                f[k] = c[j]
                j = j + 1
                k = k + 1

            for k in range(0, a + 2**r):
                c[k] = f[k]


def main():
    c = [3, 10, 13, 5, 2, 31, 4, 1, 6, 20, 16, 15, 12, 40, 50, 42]

    print c

    merge_sort(c)

    print c


if __name__ == "__main__":
    main()
