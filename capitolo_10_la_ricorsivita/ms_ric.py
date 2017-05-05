# Programma MS_RIC in Python
# Figura 10.7 del libro "Il Pensiero Computazionale: dagli algoritmi al coding"
# Autori: Paolo Ferragina e Fabrizio Luccio
# Edito da Il Mulino


# carica le funzioni matematiche
import math


def fusione(a, b):
    """
    fonde due sequenze ordinate A e B in una sequenza F, essa stessa ordinata.
    :param a: sequenza ordinata
    :param b: sequenza ordinata
    :return: f e' la sequenza ordinata contenente gli elementi di a unito b.
    """

    m = len(a)  # n indica il numero di elementi di a e b

    f = [None] * (m + m)  # inizializza il vettore ausiliario f
    i = j = k = 0

    while (i < m) and (j < m):
        if a[i] <= b[j]:  # il minore e' a[i]
            f[k] = a[i]
            i = i + 1
        else:
            f[k] = b[j]
            j = j + 1
        k = k + 1

    while i < m:
        f[k] = a[i]
        i = i + 1
        k = k + 1

    while j < m:
        f[k] = b[j]
        j = j + 1
        k = k + 1

    return f


def ms_ric(c, i, j):
    """
    Versione ricorsiva dell'ordinamento per fusione di un vettore c di n = 2^h elementi.
    il programma e' scritto per ordinare un sotto-vettore generico c[i:j], estremi inclusi
    :param c: vettore da ordinare
    :param i: limite inferiore c
    :param j: limite superiore c
    """

    if i < j:
        m = int(math.floor((i + j) / 2))
        ms_ric(c, i, m)
        ms_ric(c, m + 1, j)
        f = fusione(c[i:m + 1], c[m + 1:j + 1])
        c[i:j + 1] = f  # trasferimento in c degli elementi di f


def main():
    c = [3, 10, 13, 5, 2, 31, 4, 1, 6, 20, 16, 15, 12, 40, 50, 42]

    print "\n Sequenza in input da ordinare: ", c

    ms_ric(c, 0, len(c))

    print "\n Sequenza ordinata: ", c


if __name__ == "__main__":
    main()
