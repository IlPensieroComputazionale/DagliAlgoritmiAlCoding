# Programma FUSIONE in Python
# Figura 5.4 del libro "Il Pensiero Computazionale: dagli algoritmi al coding"
# Autori: Paolo Ferragina e Fabrizio Luccio
# Edito da Il Mulino


def fusione(a, b):
    """
    Fonde due sequenze ordinate A e B in una sequenza F, essa stessa ordinata.
    :param a: sequenza ordinata
    :param b: sequenza ordinata
    :return: f e' il vettore ordinato contenente gli elementi di a unito b.
    """

    m = len(a)                  # m indica il numero di elementi di a e di b

    f = [None] * (m + m)        # inizializza il vettore ausiliario f
    i = j = k = 0

    while (i < m) and (j < m):
        if a[i] <= b[j]:        # il minore e' a[i]
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


def main():

    a = [1, 5, 7]
    b = [2, 3, 4]

    print a, b

    f = fusione(a, b)

    print f


if __name__ == "__main__":
    main()
