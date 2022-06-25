# Study of simple GCD Euclidean algorithm
# Recursive function to return gcd of a and b
def gcd(a, b):

    # Everything divides 0
    if (a == 0):
        return b
    if (b == 0):
        return a

    # base case
    if (a == b):
        return a

    # a is greater
    if (a > b):
        return gcd(a-b, b)
    return gcd(a, b-a)


# Driver program to test above function
a = 444
b = 66
if(gcd(a, b)):
    print('GCD of ', a, ' and', b, ' is', gcd(a, b))
else:
    print('Not found!!!')
