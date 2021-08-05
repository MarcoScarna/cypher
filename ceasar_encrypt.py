"""
Cifra una stringa di lettere minuscole e visualizza il risultato.
Il secondo dato in input è la chiave del cifrario di cesare.
"""

plainText = input("Enter the word: ")
key = int(input("Key: "))

code = ""
for ch in plainText:
  ordValue = ord(ch)
  cipherValue = ordValue + key
  if cipherValue > ord('z'):
    cipherValue = ord('a') + key - (ord('z') - ordValue - 1)
  code += chr(cipherValue)

print(code)