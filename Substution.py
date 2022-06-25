# Message to encrypt

message = input('Message: ').lower()
dict1 = {}
dict2 = {}
p1 = 'abcdefghijklmnopqrstuvwxyz'
s1 = 'kjpluvtrxysqcewnfbgdzmahio'

for i in range(len(p1)):
    dict1[p1[i]] = s1[i]

# encryption
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

# decryption
for i in range(len(s1)):
    dict2[s1[i]] = p1[i]

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