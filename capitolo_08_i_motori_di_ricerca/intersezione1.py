# Programma INTERSEZIONE1 in Python
# Figura 8.5 del libro "Il Pensiero Computazionale: dagli algoritmi al coding"
# Autori: Paolo Ferragina e Fabrizio Luccio
# Edito da Il Mulino


def intersezione1(a, b):
    """
    Stampa tutti gli elementi del vettore a che sono contenuti anche nel vettore b.
    La ricerca viene eseguita confrontando ogni elemento di a con tutti gli elementi di b.
    I vettori possono non essere ordinati poiche' tutti gli elementi sono esaminati in sequenza.
    e verificando la loro uguaglianza.
    :param a: vettore a di n elementi
    :param b: vettore b di m elementi
    """

    n = len(a)
    m = len(b)

    for i in range(0, n):
        for j in range(0, m):
            if a[i] == b[j]:
                print a[i]


def main():

    # I vettori sono volutamente non ordinati
    pisa = [3, 9, 1, 200, 144]
    torre = [15, 9, 11, 101, 150, 21, 27, 500, 800, 89, 811]

    intersezione1(torre, pisa)


if __name__ == "__main__":
    main()
