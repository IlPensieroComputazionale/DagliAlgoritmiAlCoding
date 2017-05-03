# Programma TH_ITER in Python
# Figura 10.5 del libro "Il Pensiero Computazionale: dagli algoritmi al coding"
# Autori: Paolo Ferragina e Fabrizio Luccio
# Edito da Il Mulino


def th_iter(n, p):
    """
    Algoritmo iterativo per risolvere il problema della Torre di Hanoi
    L'ordine in cui si considerano i pioli e' diverso per n pari o dispari.
    :param n: numero dischi
    :param p: vettore di pioli
    """

    k = 0

    index = 1 if n % 2 == 1 else 2  # se n e' dispari, A,B,C, altrimenti A,C,B

    iter_index = 0
    while len(p[index]) < n:

        print iter_index, p[0], p[1], p[2]

        p[(k + 1) % 3].append(p[k].pop())

        if (len(p[k]) > 0) and (len(p[(k + 2) % 3]) > 0):
            if p[k][-1] < p[(k + 2) % 3][-1]:
                p[(k + 2) % 3].append(p[k].pop())
            else:
                p[k].append(p[(k + 2) % 3].pop())
        elif (len(p[k]) > 0) and (len(p[(k + 2) % 3]) == 0):
            p[(k + 2) % 3].append(p[k].pop())
        elif (len(p[k]) == 0) and (len(p[(k + 2) % 3]) > 0):
            p[k].append(p[(k + 2) % 3].pop())

        k = (k + 1) % 3
        iter_index = iter_index + 1


def main():
    a = [5, 4, 3, 2, 1]
    b = []
    c = []

    p = [a, b, c]

    th_iter(len(a), p)

    print ''
    print a
    print b
    print c


if __name__ == "__main__":
    main()
