# Programma PERMUTAZIONI in Python
# Figura 10.8 del libro "Il Pensiero Computazionale: dagli algoritmi al coding"
# Autori: Paolo Ferragina e Fabrizio Luccio
# Edito da Il Mulino


def esamina(p):
    print p


def permutazioni(p, k):
    """
    Permutazioni degli elementi di un sottovettore p[k:n-1], estremi inclusi
    :param p: vettore da permutare
    :param k: indice inferiore del vettore p
    """

    n = len(p)

    if k == n - 1:
        esamina(p)
    else:
        for i in range(k, n):
            p[i], p[k] = p[k], p[i]     # scambia p[k] con p[i]
            permutazioni(p, k + 1)
            p[i], p[k] = p[k], p[i]     # ripristina la situazione originaria


def main():

    citta = ['FI', 'MI', 'PA']

    permutazioni(citta, 0)


if __name__ == "__main__":
    main()
