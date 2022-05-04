from math import floor
def inverse(a,p):
        u = a
        v = p
        x1 = 1
        x2 = 0
        while u != 1:
            q = floor(v/u)
            r = v - u*q
            x = x2 - x1*q
            v = u
            u = r
            x2 = x1
            x1 = x
        return (x1%p) 

key = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
def encrypt( a, b, P):
    result = ''
    for i in P:
        if i != ' ':
            j = (a*key.index(i) + b) % len(key)
            result += key[j]   
        else:
            result += ' ' 
    return result
def decrypt( a, b, C):
    result = ''
    a = inverse(a,len(key))
    for i in C:
        if i != ' ':    
            j = a *(key.index(i) - b) % len(key)
            result += key[j]
        else:
            result += ' '    
    return result
def show_result( P, a, b):
    encrypted = encrypt(a,b,P)
    decrypted = decrypt(a,b,encrypted)
    decrypting = decrypt(a,b,decrypted)

    print("Plaintext: ", P)
    print("Encrypted: ", encrypted)
    print("Decrypted: ", decrypted)
    print("Decrypted: ", decrypting)

if __name__== '__main__':
    show_result('NX', 3,20)