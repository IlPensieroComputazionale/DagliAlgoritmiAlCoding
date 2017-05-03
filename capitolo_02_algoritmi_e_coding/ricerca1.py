# Programma RICERCA1 in Python
# Figura 2.2 del libro "Il Pensiero Computazionale: dagli algoritmi al coding"
# Autori: Paolo Ferragina e Fabrizio Luccio
# Edito da Il Mulino


def ricerca1(insieme, dato):
    """
    Ricerca di un elemento dato in un insieme
    :param insieme: insieme su cui ricercare
    :param dato: dato da ricercare
    """

    n = len(insieme)                        # n indica il numero di elementi di insieme

    i = 0
    while (i <= n - 1):
        if (insieme[i] == dato):
            print "%s e' presente" % dato
            return
        else:
            i = i + 1

    print "%s non e' presente" % dato


def main():

    citta = ['FI', 'MI', 'PA', 'NA', 'BO', 'TO', 'VE', 'CA']

    ricerca1(citta, 'NA')

    ricerca1(citta, 'RC')


if __name__ == "__main__":
    main()