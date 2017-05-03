# Programma RICERCA2 in Python
# Figura 2.4 del libro "Il Pensiero Computazionale: dagli algoritmi al coding"
# Autori: Paolo Ferragina e Fabrizio Luccio
# Edito da Il Mulino


def ricerca2(insieme, info, dato):
    """
    Ricerca dell'informazione associata a un elemento dato
    :param insieme: insieme su cui ricercare
    :param info: vettore di informazioni
    :param dato: dato da ricercare
    """

    n = len(insieme)       # n indica il numero di elementi di insieme

    i = 0
    while (i <= n - 1):
        if (insieme[i] == dato):
            print "l'informazione di %s e' %s" % (dato, info[i])
            return
        else:
            i = i + 1

    print "%s non e' presente" % dato


def main():

    citta = ['FI', 'MI', 'PA', 'NA', 'BO', 'TO', 'VE', 'CA']
    prefissi = ['055', '02', '091', '081', '051', '011', '041', '070']

    ricerca2(citta, prefissi, 'NA')

    ricerca2(citta, prefissi, 'RC')


if __name__ == "__main__":
    main()