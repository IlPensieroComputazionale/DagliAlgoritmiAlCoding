# Programma in Python che include BWT_INVERSA e aggiunge una serie di altri programmi
# che consentono di calcolare la BWT_diretta e stampare i risultati intermedi
# Figura 9.8 del libro "Il Pensiero Computazionale: dagli algoritmi al coding"
# Autori: Paolo Ferragina e Fabrizio Luccio
# Edito da Il Mulino


# carica librerie matematiche
import numpy as np


def bwt_diretta(t):
    """
    Algoritmo di Burrows-Wheeler per la permutazione di un testo t in una stringa l.
    :param t: testo da trasformare
    :return: l ultima, ed f prima, colonna della matrice M costruita a partire da t
    """

    riga = t + '#'                          # aggiunge il carattere speciale

    M_str = list()                          # crea la matrice con tutte le rotazioni del testo
    print "\n\nMatrice M non ordinata"
    for i in range(0, len(riga)):
        nuova_riga = riga[i:] + riga[:i]
        print " ", nuova_riga
        M_str.append(riga[i:] + riga[:i])

    M = list()
    M_str = sorted(M_str)                   # ordina la matrice

    print "\n\nMatrice M ordinata alfabeticamente"
    for i in range(0, len(riga)):
        print " ", M_str[i]

    for i in range(0, len(riga)):
        M.append(list(M_str[i]))

    M = np.asmatrix(M)

    l = M[:, -1].tostring()                 # estrae l'ultima colonna
    f = M[:, 0].tostring()                  # estrae la prima colonna

    return l, f


def posizione_prima_occorrenza(s, f):
    """
    Restituisce la posizione in f della prima occorrenza del simbolo s.
    :param s: simbolo da cercare
    :param f: stringa ove cercare
    :return: posizione in f della prima occorrenza del carattere s
    """

    for i in range(0, len(f)):
        if f[i] == s:
            return i

    return -1


def rango(l, r):
    """
    Calcola il numero di volte che la lettera l[r] appare nel prefisso l[0:r-1].
    :param l: ultima colonna della matrice M ordinata alfabeticamente
    :param r: indice del simbolo di cui calcolare il rango
    :return: numero di volte che il simbolo l[r] appare nel prefisso l[0: r-1]
    """

    conta = 0
    for i in range(0, r):
        if l[i] == l[r]:
            conta += 1

    return conta


def bwt_inversa(l, f):
    """
    Algoritmo che inverte la Trasformata di Burrows-Wheeler, contenuta nella stringa l, riottenendo il testo t.
    :param l: ultima colonna della matrice M ordinata alfabeticamente
    :param f: prima colonna matrice M ordinata alfabeticamente (e quindi essa stessa ordinata alfabeticamente)
    :return: tc testo decompresso
    """

    n = len(l)
    i = n - 1
    r = 0

    t = dict()

    sigma = set(list(l))
    c = dict()
    for s in sigma:
        c[s] = posizione_prima_occorrenza(s, f)

    while i > 0:                    # il simbolo t[0] sarebbe '#'
        t[i] = l[r]
        i = i - 1
        r = c[l[r]] + rango(l, r)

    t = ''.join([t[i] for i in t])
    return t


def main():
    t = 'LABELLABALLA'
    print "\n\nTesto da trasformare: ", t

    l, f = bwt_diretta(t)

    print "\n Prima colonna della matrice M ordinata: ", f
    print "\n BWT del testo t: ", l

    t2 = bwt_inversa(l, f)
    print "\n Testo originale (per controllo correttezza): ", t2


if __name__ == "__main__":
    main()
