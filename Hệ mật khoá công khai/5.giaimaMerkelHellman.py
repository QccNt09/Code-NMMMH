n = 6
M = 737
W = 635
daysieutang = [12,17,33,74,157,316]
hoanvi = [3,6,1,2,5,4]
ke = [319, 196, 250, 477, 200, 559]
kd = ([3, 6, 1, 2, 5, 4], 737, 635, [12, 17, 33, 74, 157, 316])
c = 1605
def decrypt_Merkle_Hellman(kd,c):
    hoanvi, M, W, daysieutang = kd
    d = c*pow(W,-1,M)%M
    #giải bài toán xếp balo
    S = d
    arr = []
    for i in range(len(daysieutang)):
        if S >= daysieutang[i]:
            arr.append('1')
            S = S-daysieutang[i]
        else:
            arr.append('0')
    a = ['']*len(arr)
    for i in range(len(arr)):
        a[i] = arr[hoanvi[i]-1]
    return ''.join(a)
m = decrypt_Merkle_Hellman(kd,c)
print(f'bản rõ : {m}(2)')
