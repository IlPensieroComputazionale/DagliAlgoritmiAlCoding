# Programma QUADRATICO in Python
# Figura 4.3 del libro "Il Pensiero Computazionale: dagli algoritmi al coding"
# Autori: Paolo Ferragina e Fabrizio Luccio
# Edito da Il Mulino


def quadratico(d):
    """
    Calcola la porzione d[a : v] avente somma massima
    provando tutti i possibili intervalli [i,j] in [1,n-1] estremi inclusi
    :param d: vettore di numeri positivi e negativi, d[0] valore iniziale dell'azione
    """

    n = len(d)                       # n indica il numero di elementi di d

    max_somma = -float('inf')
    a = 1
    v = 0

    for i in range(1, n):
        tmp = 0                      # tmp e' un valore temporaneo
        for j in range(i, n):
            tmp = tmp + d[j]
            if tmp > max_somma:
                max_somma = tmp
                a = i
                v = j

    print "Il guadagno massimo e' %d" % max_somma
    print "Esso si realizza nell'intervallo di giorni [%d,%d]" % (a, v)
    print "Porzione di d avente somma massima %s" % d[a:v+1]  # stampare elementi in d[a,v] estremi inclusi


def main():

    d = [10, +4, -6, +3, +1, +3, -2, +3, -4, +1, -9, +6]

    quadratico(d)


if __name__ == "__main__":
    main()