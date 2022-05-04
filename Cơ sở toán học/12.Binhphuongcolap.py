def modular_pow(a, k, n):
    binary=list(reversed(bin(k)[2:]))
    b = 1
    if k == 0:
        return b
    A = a
    if binary[0] == '1':
        b = a
    print('i = %5d, ki = %5d, A = %5d, b = %5d'%(0,int(binary[0]),A,b))
    for i in range(1, len(binary)):
        A = (A**2) % n
        if binary[i] == '1':
            b = A*b % n
        print('i = %5d, ki = %5d, A = %5d, b = %5d'%(i,int(binary[i]),A,b))
    
    
    
    return b



a=int(input('Nhap a: '))
k=int(input('Nhap k: '))
n=int(input('Nhap n: '))
print(modular_pow(a,k,n))