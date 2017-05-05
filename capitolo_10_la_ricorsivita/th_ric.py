# Programma TH_RIC in Python
# Figura 10.3 del libro "Il Pensiero Computazionale: dagli algoritmi al coding"
# Autori: Paolo Ferragina e Fabrizio Luccio
# Edito da Il Mulino


def th_ric(i, x, y, z):
    """
    Una soluzione ricorsiva per il problema della Torre di Hanoi. 
    I dischi sono n e i pioli sono a,b,c, ma il programma si riferisce a una fase generica in 
    cui si spostano gli i dischi piu' piccoli da un piolo x a un piolo y utilizzando un piolo z come appoggio temporaneo.
    :param i: numero dischi
    :param x: piolo x
    :param y: piolo y
    :param z: piolo z
    """
    if i == 1:
        y.append(x.pop())   # situazione limite con un solo disco
        return

    th_ric(i - 1, x, z, y)
    y.append(x.pop())
    th_ric(i - 1, z, y, x)


def main():

    a = [4, 3, 2, 1]
    b = []
    c = []

    print a
    print b
    print c
    print ''

    th_ric(4, a, b, c)

    print a
    print b
    print c


if __name__ == "__main__":
    main()
