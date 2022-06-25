from __future__ import division
from random import SystemRandom

cryptogen = SystemRandom()

# find a prime
p = 809

# random g
g = 356

# private key d from {1..,p-2}
d = 78

# public key part
k = (g ** d) % p

# k_rpiv d
# k_pub: p, g, k

# message
m = 20
# r is any real number
r = 90
# encryption
e = (g ** r) % p
# cipher
c = (k ** r * m) % p

# decryption
s = (e ** d) % p
dec = ((e ** d) ** (p - 2) * c) % p
print(m, e, c, dec)