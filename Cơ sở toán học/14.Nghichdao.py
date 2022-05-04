import math
def inverse(a,p):
    u = a
    v = p
    x1 = 1
    x2 = 0
    while u != 1:
        q = math.floor(v/u)
        r = v - u*q
        x = x2 - x1*q
        v = u
        u = r
        x2 = x1
        x1 = x
    return (x1%p)  
if __name__=='__main__':
    p = 120
    a = 11
    print(inverse(a,p))
    # print((312121305*95)%45613)