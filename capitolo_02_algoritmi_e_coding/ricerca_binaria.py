# Programma RICERCA_BINARIA in Python
# Figura 2.8 del libro "Il Pensiero Computazionale: dagli algoritmi al coding"
# Autori: Paolo Ferragina e Fabrizio Luccio
# Edito da Il Mulino


# carica le funzioni matematiche

import math


def ricerca_binaria(insieme, dato):
    """
    Ricerca binaria di un elemento dato in insieme
    :param insieme: insieme su cui ricercare (ordinato)
    :param dato: dato da ricercare
    """

    # n indica il numero di elementi di insieme
    n = len(insieme)

    i = 0
    j = n - 1

    while (i <= j):
        # math.floor() restituisce l'intero <= x piu' vicino a x
        # int() rimuove la virgola
        # m e' la posizione centrale tra i e j

        m = int(math.floor((i + j) / 2))

        if (dato == insieme[m]):
            print "%s e' presente" % dato
            return
        if (dato < insieme[m]):
            j = m - 1
        if (insieme[m] < dato):
            i = m + 1

    print "%s non e' presente" % dato


def main():

    citta = ['FI', 'MI', 'PA', 'NA', 'BO', 'TO', 'VE', 'CA']

    ricerca_binaria(citta, 'NA')

    ricerca_binaria(citta, 'RC')


if __name__ == "__main__":
    main()