# Programma GRADI in Python
# Figura 7.5 del libro "Il Pensiero Computazionale: dagli algoritmi al coding"
# Autori: Paolo Ferragina e Fabrizio Luccio
# Edito da Il Mulino


# carica le funzioni matematiche
import numpy as np


def gradi(M):
    """
    Programma per il controllo della parita' del grado di tutti i nodi di un grafo di n nodi.
    :param M: matrice di dimensione n x n
    :return: g vettore di output ove si inseriscono i gradi dei nodi
    """

    n, n = M.shape
    g = [0] * n                         # vettore di output ove si inseriscono i gradi dei nodi

    for i in range(0, n):
        grado = 0                       # indica il grado del nodo i
        for j in range(0, n):
            grado = grado + M[i, j]     # calcolo del grado g per il nodo i
        if (grado % 2 == 1):
            print "Il grafo contiene un nodo di grado dispari"
            return g
        else:
            g[i] = grado

    print "Tutti i nodi del grafo hanno grado pari"
    return g


def main():

    M1 = np.asmatrix([
        [0, 1, 1, 0],
        [1, 0, 0, 0],
        [1, 0, 0, 1],
        [0, 0, 1, 0]])

    gradi(M1)

    M2 = np.asmatrix([
        [0, 1, 1, 0],
        [1, 0, 0, 1],
        [1, 0, 0, 1],
        [0, 1, 1, 0]])

    gradi(M2)


if __name__ == "__main__":
    main()
