# Programma CODIFICA_LZ in Python Figura 9.5
# Figura 9.5 del libro "Il Pensiero Computazionale: dagli algoritmi al coding"
# Autori: Paolo Ferragina e Fabrizio Luccio
# Edito da Il Mulino


def trova_la_piu_lunga_sottostringa(t, i):
    n = len(t)
    j = i - 1
    max_l = 0
    max_dist = 0
    while j >= 0:
        for l in range(1, n-i+1):
            if t[i: i + l] == t[j: j + l]:
                if l > max_l:
                    max_l = l
                    max_dist = i-j

        j = j - 1
    return max_l, max_dist


def codifica_lz(t):
    """
    Algoritmo di Lempel e Ziv per la trasformazione dal testo t in una sequenza c di coppie.
    :param t: testo da comprimere
    :return: coppie aventi la forma (0 o distanza precedente apparizione, singola lettera o lunghezza sottostringa ripetuta) 
    """

    n = len(t)
    i = 0
    c = list()

    while i < n:
        l, dist = trova_la_piu_lunga_sottostringa(t, i)    # trova la piu' lunga sottostringa ripetuta che occorre in i
        if l == 0:                                         # t[i] appare per la prima volta
            c.append((0, t[i]))
            i = i + 1
        else:                                              # ossia, esiste copia di lunghezza l > 0
            c.append((dist, l))
            i = i + l

    return c


def main():
    t = 'LABELLABALLA'
    print "\n Testo in input: ", t

    c = codifica_lz(t)
    print "\n Sequenza di coppie: ", c


if __name__ == "__main__":
    main()
