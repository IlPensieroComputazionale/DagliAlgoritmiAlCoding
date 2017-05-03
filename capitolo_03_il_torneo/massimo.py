# Programma MASSIMO in Python
# Figura 3.2 del libro "Il Pensiero Computazionale: dagli algoritmi al coding"
# Autori: Paolo Ferragina e Fabrizio Luccio
# Edito da Il Mulino


def massimo(insieme):
    """
    Ricerca del massimo in un insieme di interi
    :param insieme: insieme di interi su cui ricercare il massimo
    """

    # n indica il numero di elementi di insieme
    n = len(insieme)

    max_val = insieme[0]

    # fa variare i da 1 a n-1
    for i in range(1, n):
        if (insieme[i] > max_val):
            max_val = insieme[i]

    print "l'elemento massimo e' %d" % max_val


def main():

    insieme = [24, 15, 7, 9, 20, 49, 33, 35, 22, 40, 52, 12, 62, 30, 8, 43]

    massimo(insieme)

    # soluzione equivalente in python
    # print "l'elemento massimo e' %d" % max(insieme)


if __name__ == "__main__":
    main()