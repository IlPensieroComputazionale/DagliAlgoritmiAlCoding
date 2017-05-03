# Programma DISPOSIZIONI_BINARIE in Python
# Figura 6.7 del libro "Il Pensiero Computazionale: dagli algoritmi al coding"
# Autori: Paolo Ferragina e Fabrizio Luccio
# Edito da Il Mulino


def disposizioni_binarie(n):
    """
    Programma per la costruzione e la stampa di tutte le disposizioni 
    binarie di n bit in un vettore v, nell'ordine dei numeri binari crescenti.
    :param n: numero di bit del vettore
    """

    v = [0] * n
    print v[::-1]           # stampa la prima disposizione 00...0

    i = 0
    while i <= n - 1:
        if v[i] == 0:       # per i > 0, si ha v[j] = 0 per j < i
            v[i] = 1
            print v[::-1]   # stampa la disposizione appena costruita
            i = 0           # ritorna al bit meno significativo
        else:
            v[i] = 0        # il bit 1 in posizione i si trasforma in 0
            i = i + 1       # passa al bit successivo


def main():

    disposizioni_binarie(4)


if __name__ == "__main__":
    main()
