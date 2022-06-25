# Study of Simple XOR cipher

plaintext = input('Enter Message:')
key = input('Enter a key:')
keylength = len(key)
newMessage = []

# encryption
for i in range(len(plaintext)):
    j = i % keylength
    cipher = ord(plaintext[i]) ^ ord(key[j])
    newMessage.append(chr(cipher))

encrypted = ''.join(newMessage)
print('Encrypted text: ', encrypted)

# decryption
newMessage = []
for i in range(len(plaintext)):
    j = i % keylength
    cipher = ord(encrypted[i]) ^ ord(key[j])
    newMessage.append(chr(cipher))

decrypted = ''.join(newMessage)
print('Decrypted text: ', decrypted)