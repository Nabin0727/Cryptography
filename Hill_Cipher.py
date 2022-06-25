# Study of Hill Cipher

import sympy
alpha='abcdefghiklmnopqrstuvwxyz'
beta={}
a='a'
for i in range(0,26):
    beta[i]=chr(ord(a)+i)
#print(beta)
#plaintext=input('Enter the plain text');
plaintext='ASIAN'
cipher=[]
key=[[5,7],[2,1]]

#adkey=[[9,2],[1,15]]
key1=sympy.Matrix(key)
print("Original matrix is:",key)
d=key1.adjugate()
print("Adjoint of a matrix is:", d)
c=key1.det()
c1=sympy.Mod(c,26)
print("Determinant of key matrix= ",c1)
c2=sympy.mod_inverse(c1,26)
print("Inverse of determinant in modulo 26: ", c2)
c3=c2*d
#print(c3)
adkey=sympy.Mod(c3,26)
adkey=adkey.tolist()
print("Inverse of key matrix in modulo 26: ",adkey)
a=plaintext.lower()
if(len(a)%2==1):
    a=a+'x'
print('Plaintext =',a)
print('Length of plain text=',len(a))
c=[]
l=[]
pt=[]
final=[]
for i in range(0,int(len(a)/2)):
    c.append([])
    l.append([])
    pt.append([])
    final.append([])
i=0
j=0
while(i<int(len(a)/2)):        
    l[i].append(0)
    l[i].append(0)
    c[i].append(ord(a[j]))
    j=j+1
    c[i].append(ord(a[j]))
    j=j+1
    i=i+1
for i in range(int(len(a)/2)):
  #  print(c[i][0]-97)
    c[i][0]=(c[i][0]-97)
    c[i][1]=(c[i][1]-97)
#else:
#       break
# matrix multiplication
ct=''
for i in range(int(len(a)/2)):
    for j in range(len(c[0])):
        pt[i].append(0)
        final[i].append(0)
        for k in range(len(c[0])):
            l[i][j]=sympy.Mod((l[i][j]+(c[i][k]*key[k][j])),26)
        cipher.append(beta[l[i][j]])
#        print(cipher)
        ct=ct+beta[l[i][j]]
print('Cipher text in in numeric array=',l)
print('Cipher',cipher,'\nctext=',ct)
print('length of cipher text',len(cipher))
k=0
for i in range(0,int(len(cipher)/2)):
    for j in range(0,2):
        pt[i][j]=(ord(cipher[k])-97)%26
        k=k+1
er=[]
dt=''
#decription to plain text
for i in range(int(len(a)/2)):
    for j in range(2):
        for k in range(2):
            final[i][j]=(final[i][j]+(pt[i][k]*adkey[k][j]))%26
        er.append(beta[final[i][j]])
        dt=dt+beta[final[i][j]]
               
print('Length of decipher text =',len(er))
print('Final palintext in numeric array=',final)
print('Decipher text =',dt)