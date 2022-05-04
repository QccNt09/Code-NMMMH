from math import ceil
def encrypt(pt,k):
    ptAfterTrim=pt.replace(' ','')
    keyCipher=(k*ceil(len(pt)/len(k)))[:len(ptAfterTrim)]
    
    cipherText = ''
    i=0
    for j in range(len(pt)):
        if pt[j]!=' ':
            cipherText += chr((ord(pt[j])+ord(keyCipher[i])-2*ord('a'))%26+ord('a'))
            i+=1
        else:
            cipherText+=' '
    return cipherText

if __name__ =='__main__':
    k='sun'
    pt='goodstudent'
    m=3
    
    print(encrypt(pt, k))