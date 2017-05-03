# Programma FIB in Python
# Figura 10.14 del libro "Il Pensiero Computazionale: dagli algoritmi al coding"
# Autori: Paolo Ferragina e Fabrizio Luccio
# Edito da Il Mulino


def fib(n):
    """
    Calcolo iterativo e stampa dell'n-esimo numero di Fibonacci.
    :param n: numero di Fibonacci
    """

    a = 1
    b = 1                   # pone a = F_1 e b = F_2

    for i in range(3, n+1):
        c = a + b
        a = b
        b = c               # pone a = F_{i-1} b = F_{i}

    print "F_%d = %d" % (n, b)


def main():

    fib(12)


if __name__ == "__main__":
    main()
