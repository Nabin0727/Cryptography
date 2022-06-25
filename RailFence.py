# Simple study of RailFence Cipher

s = input("Enter your message: ").replace(" ", "")
k = int(input("Enter key: "))

def encrypt(s, k):
    # Creating a matrix
    enc = [[" " for i in range(len(s))] for j in range(k)]
    flag = 0
    row = 0
    # Putting characters in a grid
    for i in range(len(s)):
        enc[row][i] = s[i]
        if row == 0:
            flag = 0
        elif row == k-1:
            flag = 1
        if flag == 0:
            row += 1
        else:
            row -= 1

    for i in range(k):
        print("".join(enc[i]))

    ct = []
    # Eliminate spaces
    for i in range(k):
        for j in range(len(s)):
            if enc[i][j] != ' ':
                ct.append(enc[i][j])

    cipher = "".join(ct)
    return cipher

print("Cipher Text: ", encrypt(s, k))