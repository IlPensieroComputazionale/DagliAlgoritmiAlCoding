# Programma CONNESSIONE in Python
# Figura 7.4 del libro "Il Pensiero Computazionale: dagli algoritmi al coding"
# Autori: Paolo Ferragina e Fabrizio Luccio
# Edito da Il Mulino


# carica le funzioni matematiche
import numpy as np


def connessione(M):
    """
    Programma che stabilisce se un grafo di n nodi, descritto dalla matrice M, e' connesso 
    attraverso una sua visita in ampiezza.
    :param M: matrice di dimensione n x n
    """

    n, n = M.shape
    r = [0] * n                         # vettore di n celle per registrare i nodi raggiungibili da 0

    r[0] = 0
    s = 0
    f = 0
    while s <= f:                     # f inidica l'ultima cella occupata di r
        i = r[s]                        # indica il nodo esaminato
        for j in range(1, n):
            if M[i,j] > 0:            # cioe' per ogni elemento >0 nella riga i
                if j not in r[0: f]:
                    f = f + 1
                    r[f] = j
                    if f == n - 1:
                        print "il grafo e' connesso"
                        return

        s = s + 1

    print "il grafo non e' connesso"


def main():

    # Ricordarsi che il grafo deve essere non orientato
    #   e quindi le matrici M1 e M2 devono essere simmetriche
    M1 = np.asmatrix([
        [0, 1, 1, 0],
        [1, 0, 0, 0],
        [1, 0, 0, 1],
        [0, 0, 1, 0]])

    connessione(M1)

    M2 = np.asmatrix([
        [0, 1, 0, 0],
        [1, 0, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 1, 0]])

    connessione(M2)


if __name__ == "__main__":
    main()
