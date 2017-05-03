# Programma HUFFMAN in Python
# Figura 9.2 del libro "Il Pensiero Computazionale: dagli algoritmi al coding"
# Autori: Paolo Ferragina e Fabrizio Luccio
# Edito da Il Mulino


# carica librerie ausiliarie
from collections import defaultdict


def frequenze(t):
    f = defaultdict(int)
    for u in range(0, len(t)):
        f[t[u]] += 1

    return f


def huffman(sigma_f):
    """
    Algoritmo di Huffman per la compressione statistica di testi.
    :param sigma_f: sequenza di lettere con relativa frequenza
    :return: tree albero per codificare le lettere del testo
    """
    tree = {u: (sigma_f[u], None, None) for u in sigma_f}
    s = {u: sigma_f[u] for u in sigma_f}

    for i in range(1, len(sigma_f)):
        u = sorted(s, key=s.get)[0]         # scegli la coppia u e v tali che f[u] e f[v] sono minimi
        v = sorted(s, key=s.get)[1]
        w = '%s%s' % (u, v)                 # crea il nodo w
        s[w] = s[u] + s[v]                  # aggiungi la coppia w, f[w] a s
        del s[u]                            # cancella u, v da s
        del s[v]
        tree[w] = (s[w], u, v)              # inserisci in tree il nodo w come padre di u, v

    return tree


def ottieni_codice(tree):
    root = sorted(tree, key=tree.get, reverse=True)[0]
    left = tree[root][1]
    right = tree[root][2]
    codice = dict()
    ottieni_codice_ric(tree, left, '0', codice)
    ottieni_codice_ric(tree, right, '1', codice)
    return codice


def ottieni_codice_ric(tree, u, code, codice):
    left = tree[u][1]
    right = tree[u][2]
    if (left is None) and (right is None):
        codice[u] = code
        return
    ottieni_codice_ric(tree, left, '0' + code, codice)
    ottieni_codice_ric(tree, right, '1' + code, codice)


def comprimi_huffman(t, codice):
    """
    Comprime il testo t usando l'albero tree
    :param t: testo da comprimere
    :param codice: codice di compressione di huffman
    :return: tc testo compresso
    """

    tc = ''
    for i in range(0, len(t)):
        tc = tc + codice[t[i]]

    return tc


def main():

    t = 'LABELLABALLA'
    print "\n Testo in input: ", t

    sigma_f = frequenze(t)
    # print sigma_f

    tree = huffman(sigma_f)
    # print tree

    codice = ottieni_codice(tree)
    print "\n Codice di Huffman: ", codice

    tc = comprimi_huffman(t, codice)
    print "\n Testo compresso secondo Huffman: ", tc


if __name__ == "__main__":
    main()
