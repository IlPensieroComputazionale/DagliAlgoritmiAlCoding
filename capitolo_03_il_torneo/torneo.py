# Programma TORNEO in Python
# Figura 3.4 del libro "Il Pensiero Computazionale: dagli algoritmi al coding"
# Autori: Paolo Ferragina e Fabrizio Luccio
# Edito da Il Mulino


# carica le funzioni matematiche

import math


def torneo(insieme):
    """
    Ricerca del massimo in un tabellone con n = 2^k partecipanti
    :param insieme: insieme di interi su cui ricercare il massimo
    """

    n = len(insieme)                    # n indica il numero di elementi di insieme
    k = int(math.log(n, 2))             # livello delle foglie

    p = list()
    for i in range(0, n):               # copia insieme in p
        p.append(insieme[i])

    h = k                               # h e' il livello corrente
    while h >= 1:                       # esegue gli incontri al livello h, da k a 1
        i = 0
        v = list()
                                        # x**y e' l'espressione python per x^y
        while i <= 2**h - 2:            # carica in v i vincitori
            if p[i] > p[i + 1]:         # p[i] e' il vincitore
                v.append(p[i])
            else:                       # p[i+1] e' il vincitore
                v.append(p[i + 1])
            i = i + 2

        for i in range(0, 2**(h-1)):    # trasferisce in p i vincitori
            p[i] = v[i]

        h = h - 1                       # si sposta al livello superiore

    print "il massimo e' %d" % p[0]


def main():

    insieme = [24, 15, 7, 9, 20, 49, 33, 35, 22, 40, 52, 12, 62, 30, 8, 43]

    torneo(insieme)


if __name__ == "__main__":
    main()
