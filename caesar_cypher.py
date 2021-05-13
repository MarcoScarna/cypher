ALFABETH = "abcdefghijklmnopqrstuvwxyz"

class caesar_cypher:
    # Constructor
    def __init__(self, k):
        pass

    # Encodes a single letter
    def encodes_letter(self, d, k):
        letter_position = ALFABETH.find(d)
        letter_cy_position = (int(letter_position) + int(k)) % 26
        return ALFABETH[letter_cy_position]
    
    # Decodes a single letter
    def decodes_letter(self, c, k):
        letter_position = ALFABETH.find(c)
        letter_pl_position = (int(letter_position) - int(k)) % 26
        return ALFABETH[letter_pl_position]
  
    # Encodes a plaintext
    def encodes_plaintext(self, text, k):
        plaintext = ""
        cyphertext = ""
        for i in range(len(text)) :
            letter = ALFABETH.find(text[i]) 
            if letter != -1 :
                cyphertext = cyphertext + caesar_cypher.encodes_letter(
                    self , ALFABETH[letter], k
                    )
                plaintext = plaintext + text[i] 
        return cyphertext
    
    # Decodes a cyphertext
    def decodes_cyphertext(self , text, k):
        plaintext = ""
        for i in range(len(text)) :
            letter = ALFABETH.find(text[i]) 
            if letter != -1 :
                plaintext = plaintext + caesar_cypher.decodes_cyphertext(
                    self , ALFABETH[letter], k
                    )
        return plaintext


if __name__ == '__main__':

    caeser_algorithm = caesar_cypher('')


    out_per_utente = '''
    Ciao caro Utente BENVEUTO AL CIFRARIO DI CESARE , cosa desidera fare ?
    1 - codificare una lettera
    2 - decodificare una lettera
    3 - codificare un testo
    4 - decodificare un testo\n
    '''
    ricevuto = int(input(out_per_utente))
    k = input("digitare la chiave: ")

    if ricevuto == 1:
        lettera = input("digitare la lettera da codificare: ")
        print("lettera codificata: " + caeser_algorithm.encodes_letter(lettera, k))

    elif ricevuto == 2:
        lettera = input("digitare la lettera da decodificare: ")
        print("lettera decodificata: "+ caeser_algorithm.decodes_letter(lettera, k))

    elif ricevuto == 3 : 
        text = input("digitare il testo da codificare: ")
        print("testo codificato: " + caeser_algorithm.encodes_plaintext(text, k))

    elif ricevuto == 4 :
        text = input("digitare il testo da decodificare: ")
        print("testo decodificato: " + caeser_algorithm.decodes_cyphertext(text, k))

