def GCD(a,b):
    while b != 0:
        t = a%b
        a = b
        b = t
    return a
print(GCD(235125,693693))