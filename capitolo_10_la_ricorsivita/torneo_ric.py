# Programma TORNEO_RIC in Python
# Figura 10.1 del libro "Il Pensiero Computazionale: dagli algoritmi al coding"
# Autori: Paolo Ferragina e Fabrizio Luccio
# Edito da Il Mulino


# carica le funzioni matematiche
import math


def torneo_ric(insieme, i, j):
    """
    Determinazione del vincitore di un torneo in forma ricorsiva. 
    I partecipanti sono contenuti in un vettore 'insieme' di n = 2^k elementi, 
    ma il programma si riferisce a un generico sotto-torneo tra i partecipanti 
    contenuti nella zona insieme[i:j], estremi inclusi.
    :param insieme: insieme di interi su cui ricercare il massimo
    :param i: indice inferiore del tabellone 'insieme'
    :param j: indice superiore del tabellone 'insieme'
    """

    if j == i + 1:                       # situazione limite con due giocatori
        if insieme[i] > insieme[j]:
            return insieme[i]
        else:
            return insieme[j]

    m = int(math.floor((i + j) / 2))
    v1 = torneo_ric(insieme, i, m)          # v1 e' il vincitore del primo sotto-torneo
    v2 = torneo_ric(insieme, m + 1, j)      # v2 e' il vincitore del secondo sotto-torneo

    if v1 > v2:
        return v1
    else:
        return v2


def main():

    insieme = [24, 15, 7, 9, 20, 49, 33, 35, 22, 40, 52, 12, 62, 30, 8, 43]

    print "il massimo e' %d" % torneo_ric(insieme, 0, len(insieme) - 1)


if __name__ == "__main__":
    main()
