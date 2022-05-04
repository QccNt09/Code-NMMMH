alpha = 39
p = 211
a = 113 #khoá bí mật
beta = pow(alpha,a,p)
ke = (p,alpha,beta) #khoá công khai
print(ke)
def encrypt(x,ke):
    k = 23
    p = ke[0]
    alpha = ke[1]
    beta = ke[2]
    y1 = pow(alpha,k,p)
    y2 = x*pow(beta,k,p)%p
    return (y1,y2)
encrypt(34,ke)
