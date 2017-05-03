# Programma LINEARE in Python
# Figura 4.5 del libro "Il Pensiero Computazionale: dagli algoritmi al coding"
# Autori: Paolo Ferragina e Fabrizio Luccio
# Edito da Il Mulino


def lineare(d):
    """
    Calcola la porzione d[a : v] avente somma massima
    provando tutti i possibili intervalli [i,j] in [1,n-1] estremi inclusi
    :param d: vettore di numeri positivi e negativi, d[0] valore iniziale dell'azione
    """

    n = len(d)  # n indica il numero di elementi di d

    max_somma = -float('inf')
    a = 1
    v = 0

    atmp = a  # atmp e' un indice temporaneo
    tmp = 0  # tmp e' un valore temporaneo

    for i in range(1, n):
        tmp = tmp + d[i]
        if tmp > max_somma:
            max_somma = tmp
            a = atmp
            v = i
        if tmp < 0:
            tmp = 0
            atmp = i + 1

    print "Il guadagno massimo e' %d" % max_somma
    print "Esso si realizza nell'intervallo di giorni [%d,%d]" % (a, v)
    print "Porzione di d avente somma massima %s" % d[a:v + 1]  # stampiamo gli elementi in d[a:v] estremi inclusi


def main():
    d = [10, +4, -6, +3, +1, +3, -2, +3, -4, +1, -9, +6]

    lineare(d)


if __name__ == "__main__":
    main()
