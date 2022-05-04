def xepbalo(arr,s,n):
    v = []
    for i in range(n-1,-1,-1):
            if(s>= arr[i]):              
                a = 1
                v.append(a)
                s = s - arr[i]
            else:
                a = 0
                v.append(a)    
    return list(reversed(v))
arr = [33, 74, 157, 316, 620, 1230, 2460]
s = 1653
n = len(arr)
print(xepbalo(arr,s,n))