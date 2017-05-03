# Programma QUICK_SORT in Python
# Figura 10.12 del libro "Il Pensiero Computazionale: dagli algoritmi al coding"
# Autori: Paolo Ferragina e Fabrizio Luccio
# Edito da Il Mulino


# carica le funzioni matematiche
import numpy as np


def partizione(c, p, q):
    """
    Riorganizza un vettore c nella parte compresa tra gli indici p e q, attorno a un elemento perno scelto a caso.
    Gli elementi minori o uguali al perno vengono posti alla sua sinistra e gli elementi maggiori alla sua destra.
    :param c: vettore da partizionare
    :param p: indice inferiore del vettore c
    :param q: indice superiore del vettore c
    """

    r = np.random.randint(p, q + 1)

    c[r], c[q] = c[q], c[r]                 # ora il perno si trova in c[q]

    i = p - 1
    for j in range(p, q):
        if (c[j] <= c[q]):
            i = i + 1
            if i < j:
                c[i], c[j] = c[j], c[i]

    s = i + 1                               # posizione finale perno
    c[q], c[s] = c[s], c[q]                 # ora il perno si trova in c[s]
    return s


def quick_sort(c, p, q):
    """
    Ordina il vettore c usando la funzione partizione.
    :param c: vettore da ordinare
    :param p: indice inferiore del vettore c
    :param q: indice superiore del vettore c
    """

    if p < q:
        s = partizione(c, p, q)
        quick_sort(c, p, s - 1)
        quick_sort(c, s + 1, q)


def main():
    c = [3, 10, 13, 5, 2, 31, 4, 1, 6, 20, 16, 15, 12, 40, 50, 42]

    print "\n Vettore in input da ordinare: ", c

    quick_sort(c, 0, len(c) - 1)

    print "\n Vettore ordinato: ", c


if __name__ == "__main__":
    main()
