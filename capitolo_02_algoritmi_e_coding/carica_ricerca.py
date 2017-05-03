# Programma CARICA_RICERCA in Python
# Figura 2.6 del libro "Il Pensiero Computazionale: dagli algoritmi al coding"
# Autori: Paolo Ferragina e Fabrizio Luccio
# Edito da Il Mulino


# copia il programma ricerca2 dal file precedente
from ricerca2 import ricerca2


def carica_ricerca():
    """
    Programma per interrogare il computer sull'informazione associata 
    ai nomi di un elenco attraverso la chiamata di ricerca2
    :return: 
    """
    citta = ['FI', 'MI', 'PA', 'NA', 'BO', 'TO', 'VE', 'CA']
    prefissi = ['055', '02', '091', '081', '051', '011', '041', '070']

    # cerca e' un parametro di controllo.
    # Per cerca == 'VAI' la ricerca prosegue
    # Per cerca == 'ALT' la ricerca si arresta
    cerca = 'VAI'

    while cerca == 'VAI':
        nome = raw_input('comunica il dato da cercare: ')
        ricerca2(citta, prefissi, nome)
        cerca = raw_input('vuoi continuare la ricerca? ')


def main():

    carica_ricerca()


if __name__ == "__main__":
    main()


"""
Esempio di interazione con l'utente
python carica_ricerca.py
comunica il dato da cercare: NA
l'informazione di NA e' 081
vuoi continuare la ricerca? VAI
comunica il dato da cercare: RG
RG non e' presente
vuoi continuare la ricerca?  ALT
Process finished with exit code 0
"""