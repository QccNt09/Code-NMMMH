def decrypt(y,a,p):
    y1 = y[0]
    y2 = y[1]
    x = y2*pow(y1,-a,p)%p
    return x
y = (145, 140)
a = 113
p = 211
decrypt(y,a,p)
