# Programma RB_RIC in Python
# Figura 10.6 del libro "Il Pensiero Computazionale: dagli algoritmi al coding"
# Autori: Paolo Ferragina e Fabrizio Luccio
# Edito da Il Mulino


# carica le funzioni matematiche
import math


def rb_ric(insieme, i, j, dato):
    """
    Versione ricorsiva della ricerca binaria di un elemento dato in insieme.
    :param insieme: insieme su cui cercare (ordinato)
    :param i: indice inferiore del vettore insieme
    :param j: indice superiore del vettore insieme
    :param dato: dato da cercare
    """

    if i > j:
        print "\n %s non e' presente" % dato
        return

    m = int(math.floor((i + j) / 2))

    if dato == insieme[m]:
        print "\n %s e' presente" % dato
        return
    elif dato < insieme[m]:
        rb_ric(insieme, i, m - 1, dato)
    else:
        rb_ric(insieme, m + 1, j, dato)


def main():
    citta = ['FI', 'MI', 'PA', 'NA', 'BO', 'TO', 'VE', 'CA']

    print "\n Vettore su cui cercare: ", citta

    rb_ric(citta, 0, len(citta) - 1, 'NA')

    rb_ric(citta, 0, len(citta) - 1, 'RC')


if __name__ == "__main__":
    main()
