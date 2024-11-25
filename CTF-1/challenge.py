from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from binascii import hexlify

flag = open("flag.txt").read()

key = get_random_bytes(16)
iv = get_random_bytes(16)

def encrypt_flag():
  cipher = AES.new(key, AES.MODE_OFB, iv)
  return hexlify(cipher.encrypt(flag.encode(encoding="utf-8")))

def encrypt_plaintext(plaintext):
  cipher = AES.new(key, AES.MODE_OFB, iv)
  return hexlify(cipher.encrypt(plaintext.encode(encoding="utf-8")))

while True:
  print("Choose from the following commands: (f)lag or (e)ncrypt")
  command = input("Input command: ")
  if command == "f":
    encrypted_flag = encrypt_flag()
    print("Flag: " + encrypted_flag.decode("utf-8"))
  elif command == "e":
    plaintext = input("Provide plaintext: ")
    ciphertext = encrypt_plaintext(plaintext)
    print("Ciphertext: " + ciphertext.decode("utf-8"))
  else:
    print("Not a valid command.")
    break
