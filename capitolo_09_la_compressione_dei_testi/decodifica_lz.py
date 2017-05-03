# Programma DECODIFICA_LZ in Python Figura 9.5
# Figura 9.6 del libro "Il Pensiero Computazionale: dagli algoritmi al coding"
# Autori: Paolo Ferragina e Fabrizio Luccio
# Edito da Il Mulino


# carica codifica_lz
from codifica_lz import *


def decodifica_lz(c):
    """
    Algoritmo di Lempel e Ziv per la trasformazione inversa da una sequenza c di coppie al testo originale t.
    :param t: c coppie (0 o distanza precedente apparizione, singola lettera o lunghezza sottostringa ripetuta) 
    :return: testo decompresso
    """

    i = 0
    t = dict()

    while len(c) > 0:
        a, b = c.pop(0)         # estrai la prima coppia, sia (a, b)
        if a == 0:
            t[i] = b
            i = i + 1
        else:                   # copia di una sottostringa di lunghezza 'b' e distanza 'a'
            for k in range(0, b):
                t[i + k] = t[i - a + k]
            i = i + b

    t = ''.join([t[i] for i in t])
    return t


def main():
    t = 'LABELLABALLA'
    print "\n testo in input: ", t

    c = codifica_lz(t)
    print "\n sequenza di coppie: ", c

    t2 = decodifica_lz(c)
    print "\n testo da sequenza coppie (per controllo correttezza): ", t2


if __name__ == "__main__":
    main()
