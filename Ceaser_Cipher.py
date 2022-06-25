# Message to Encrypt

message = input('Enter Message Decrypt: ').lower()
key = int(input('Enter the value of the key:'))
dict1 = {}
dict2 = {}
p1 = 'abcdefghijklmnopqrstuvwxyz'

# Encryption
for i in range(len(p1)):
    dict1[p1[i]] = p1[(i+key)%len(p1)]

encrypt_text = []
for char in message:
    if char in p1:
        temp = dict1[char]
        encrypt_text.append(temp)
    else:
        temp = char
        encrypt_text.append(temp)

ciphertext = ''.join(encrypt_text)
print('Encrypted text: ', ciphertext)

# Decryption
for i in range(len(p1)):
    dict2[p1[i]] = p1[(i-key)%len(p1)]

decrypt_text = []
for char in ciphertext:
    if char in p1:
        temp = dict2[char]
        decrypt_text.append(temp)
    else:
        temp = char
        decrypt_text.append(temp)

ciphertext = ''.join(decrypt_text)
print('Decrypted text: ', ciphertext)