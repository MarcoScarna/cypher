"""
Decifra una stringa di lettere minuscole e visualizza il risultato.
Il secondo dato in input è la chiave del cifrario di cesare.
"""
code = input("Enter the cipher word: ")
key = int(input("Key: "))

plainText = ""
for ch in code:
  ordValue = ord(ch)
  plainValue = ordValue - key
  if plainValue < ord('a'):
    plainValue = ord('z') - (key - (ord('z') - ordValue - 1))
  plainText += chr(plainValue)

print(plainText)