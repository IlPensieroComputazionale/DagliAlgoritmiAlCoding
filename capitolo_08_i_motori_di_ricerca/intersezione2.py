# Programma INTERSEZIONE2 in Python
# Figura 8.6 del libro "Il Pensiero Computazionale: dagli algoritmi al coding"
# Autori: Paolo Ferragina e Fabrizio Luccio
# Edito da Il Mulino


# carica le funzioni matematiche
import math


def intersezione2(a, b):
    """
    Stampa tutti gli elementi del vettore a che sono contenuti anche nel vettore b.
    La ricerca di ogni elemento b[k] in a e' eseguita mediante l'algoritmo RICERCA_BINARIA su a 
    qui ricopiato e adattato per effettuare le stampe corrette. 
    Il vettore b puo' non essere ordinato poiche' tutti i suoi elementi sono esaminati in sequenza.
    :param a: vettore a di n elementi ordinato
    :param b: vettore b di m elementi (non necessariamente ordinato)
    """

    n = len(a)
    m = len(b)

    for k in range(0, m):
        i = 0
        j = n - 1
        while i <= j:
            c = int(math.floor((i + j) / 2))
            if b[k] == a[c]:
                print b[k]
                break              # il comando break esce dal ciclo while
            elif b[k] < a[c]:
                j = c - 1
            else:
                i = c + 1


def main():

    torre = [9, 11, 15, 21, 27, 89, 101, 150, 500, 800, 811]    # il vettore a e' ordinato
    pisa = [9, 1, 3, 144, 210]                                  # il vettore b non e' necessariamente ordinato

    intersezione2(torre, pisa)


if __name__ == "__main__":
    main()
