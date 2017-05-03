# Programma COUNTING_SORT in Python
# Figura 5.8 del libro "Il Pensiero Computazionale: dagli algoritmi al coding"
# Autori: Paolo Ferragina e Fabrizio Luccio
# Edito da Il Mulino



def counting_sort(c, k):
    """
    Ordina un vettore c di n interi maggiori o uguali a 0 e minori di k 
    tra i quali e' definita la relazione di confronto <=
    impiegando un vettore ausiliario a di k posizioni.
    :param c: vettore da ordinare
    """

    n = len(c)                                  # n indica il numero di elementi di c

    a = [0] * k                                 # inizializza il vettore ausiliario a di k posizioni

    for i in range(0, n):
        a[c[i]] = a[c[i]] + 1

    h = 0
    for j in range(0, k):
        for i in range(0, a[j]):
            c[h] = j
            h += 1


def main():

    c = [3, 2, 3, 3, 3]
    k = 4

    print c

    counting_sort(c, k)

    print c


if __name__ == "__main__":
    main()
