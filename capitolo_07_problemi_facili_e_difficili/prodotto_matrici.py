# Programma PRODOTTO_MATRICI in Python
# Figura 7.3 del libro "Il Pensiero Computazionale: dagli algoritmi al coding"
# Autori: Paolo Ferragina e Fabrizio Luccio
# Edito da Il Mulino


# carica le funzioni matematiche
import numpy as np


def prodotto_matrici(A, B):
    """
    Programma per calcolare il prodotto di due matrici.
    :param A: matrice di dimensione m x n
    :param B: matrice di dimensione n x p
    :return: C = A x B matrice di dimensione m x p
    """

    m, n = A.shape
    n, p = B.shape
    C = np.zeros((m, p))

    for i in range(0, m):
        for j in range(0, p):
            s = 0
            for k in range(0, n):
                s = s + A[i, k] * B[k, j]
            C[i, j] = s

    return C


def main():
    K = np.asmatrix([
        [0, 2, 2, 1],
        [2, 0, 0, 1],
        [2, 0, 0, 1],
        [1, 1, 1, 0]])

    K2 = prodotto_matrici(K, K)

    print K2


if __name__ == "__main__":
    main()
