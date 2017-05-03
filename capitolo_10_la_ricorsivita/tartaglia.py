# Programma TARTAGLIA in Python
# Figura 10.13 del libro "Il Pensiero Computazionale: dagli algoritmi al coding"
# Autori: Paolo Ferragina e Fabrizio Luccio
# Edito da Il Mulino


# carica le funzioni matematiche
import numpy as np


def tartaglia(n):
    """
    Costruzisce il Triangolo di Tartaglia fino alla riga n.
    :param n: righe del triangolo di tartaglia da costruire
    """

    T = np.zeros((n, n))

    for i in range(0, n):
        T[i, 0] = 1
        T[i, i] = 1

    for i in range(2, n):
        for j in range(1, i):
            T[i, j] = T[i - 1, j] + T[i - 1, j - 1]

    return T


def main():

    T = tartaglia(8)

    print T


if __name__ == "__main__":
    main()
