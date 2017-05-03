# Programma TRASFORMA in Python
# Figura 6.3 del libro "Il Pensiero Computazionale: dagli algoritmi al coding"
# Autori: Paolo Ferragina e Fabrizio Luccio
# Edito da Il Mulino


def trasforma(k, c):
    """
    Trasforma il carattere c in input nel carattere cifrato t in output
    applicando una traslazione in modulo 26 di k posizioni nell'alfabeto, 
    ove k e' la chiave del cifrario.
    :param k: chiave del cifrario
    :param c: carattere c in input
    :return: t carattere cifrato in output
    """

    alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    i = 0
    while alfabeto[i] != c:
        i = i + 1

    j = (i + k) % 26
    t = alfabeto[j]

    return t


def main():

    print trasforma(0, 'D')
    print trasforma(3, 'D')
    print trasforma(3, 'X')


if __name__ == "__main__":
    main()
