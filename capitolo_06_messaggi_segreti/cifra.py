# Programma CIFRA in Python
# Figura 6.3 del libro "Il Pensiero Computazionale: dagli algoritmi al coding"
# Autori: Paolo Ferragina e Fabrizio Luccio
# Edito da Il Mulino


# carica il programma trasforma
from trasforma import trasforma


def cifra():
    """
    Trasforma un messaggio nel relativo crittogramma
    applicando una traslazione in modulo 26 di k posizioni nell'alfabeto, 
    ove k e' la chiave del cifrario.
    """

    k = int(raw_input('comunica la chiave: '))

    msg = raw_input('comunica il messaggio: ')     # msg e' un vettore di 140 caratteri contenente il messaggio

    crt = [''] * 140                               # crt e' un vettore di 140 caratteri contenente il crittogramma
    for h in range(0, 140):
        if h < len(msg):
            t = trasforma(k, msg[h])
            crt[h] = t

    print ''.join(crt)


def main():

    cifra()


if __name__ == "__main__":
    main()


"""
Esempio di interazione con l'utente
python cifra.py
comunica la chiave: 3
comunica il messaggio: PENSIEROCOMPUTAZIONALE
SHQVLHURFRPSXWDCLRQDOH 
Process finished with exit code 0
"""