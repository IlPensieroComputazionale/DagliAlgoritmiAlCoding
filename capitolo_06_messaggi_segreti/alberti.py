# Programma ALBERTI in Python
# Figura 6.6 del libro "Il Pensiero Computazionale: dagli algoritmi al coding"
# Autori: Paolo Ferragina e Fabrizio Luccio
# Edito da Il Mulino


def alberti():
    """
    Trasforma un messaggio nel relativo crittogramma
    applicando il metodo di Leon Battista Alberti, 
    ove k e' la chiave del cifrario.
    """

    esterno = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', '1', '2', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', '3', '4', '5', 'Z']

    interno = ['F', 'B', 'M', 'K', 'R', 'O', 'A', 'V', 'T', 'Z', 'Y', 'C', 'G',
               'N', 'L', 'X', 'P', 'Q', 'H', 'J', 'D', 'I', 'E', 'U', 'S', 'W']

    k = 0   # k (la chiave) e' l'entita' della rotazione antioraria del disco interno rispetto al disco esterno

    msg = raw_input('comunica il messaggio: ')     # msg e' un vettore di 140 caratteri contenente il messaggio

    crt = [' '] * 140                              # crt e' un vettore di 140 caratteri contenente il crittogramma

    for h in range(0, 140):
        if h < len(msg):
            i = 0
            while msg[h] != esterno[i]:            # cerca msg[h] in esterno
                i = i + 1
            j = (i + k) % 26                       # ora msg[h] = esterno[i]
            crt[h] = interno[j]
            if esterno[i] in ['1', '2', '3', '4', '5']:
                k = (i + k) % 26                   # msg[h] e' un carattere speciale: l'operazione aggiorna la chiave

    print ''.join(crt)


def main():

    alberti()


if __name__ == "__main__":
    main()


"""
Esempio di interazione con l'utente
python alberti.py
comunica il messaggio: BUONA3SERA
BDLNFELFNE                                                                                                                                  
Process finished with exit code 0
"""