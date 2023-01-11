import random

### 1 ###

def millRab(n, k): #k - iterator
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for kk in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for kk in range(r - 1): 
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

### 2 ###

def primeGen():
    while True:
        a = (random.randrange(2 ** (255), 2 ** 256))
        if millRab(a,40): #40 iterations is optimal
            return a

def pqGen():
    i = 0
    while i < 4:
        key = primeGen()
        keys.append(key)
        i += 1
    if keys[0] * keys[1] <= keys[2] * keys[3]:
        return True
    else:
        keys.clear()
        pqGen()

### 3 ###

def gcdExt(a, m):
    if a == 0:
        return m, 0, 1
    gcd, x1, y1 = gcdExt(m % a, a)
    x = y1 - (m // a) * x1
    y = x1
    return gcd, x, y


def invMod(a, m):
    gcd, x, y = gcdExt(a, m)
    if gcd == 1:
        return (x % m + m) % m
    else:
        return -1

def keyGen(p, q): #GenerateKeyPair
    n = p * q
    fi = (p - 1) * (q - 1)
    while True:
        e = random.randint(2, fi - 1)
        if gcdExt(e, fi)[0] == 1:
            d = invMod(e, fi)
            return e, n, d

### 4 ###

def enc(M, e, n): #Encrypt
    C = pow(M, e, n)
    return C

def dec(C, d, n): #Decrypt
    M = pow(C, d, n)
    return M

def sign(M, d, n): #Sign
    S = pow(M, d, n)
    return S

def ver(M, S, e, n): #Verify
    return M == pow(S, e, n)

def sendKey(k, d, e1, n1, n): #SendKey
    K1 = enc(k, e1, n1)
    S = sign(k, d, n)
    S1 = enc(S, e1, n1)
    return K1, S1

def getKey(K1, S1, d1, n1, e, n): #ReceiveKey
    K = dec(K1, d1, n1)
    S = dec(S1, d1, n1)
    if ver(K, S, e, n):
        return K
    else:
        return False

if __name__ == "__main__":
    keys = []
    pqGen()
    p, q = keys[0], keys[1]
    p1, q1 = keys[2], keys[3]
    e, n ,d = keyGen(p,q)
    e1, n1, d1 = keyGen(p1,q1)

    M = random.randint(0, n)
    k = random.randint(0, n)


    print("[***]Alice keys:\np:", p, "\nq:", q, "\nn:", n, "\ne:", e, "\nd:", d)
    print("="*40)
    print("[***]Bob keys:\np:", p1, "\nq:", q1, "\nn:", n1, "\ne:", e1, "\nd:", d1)
    print("="*40)
    print("[***]\nMessage:\n",M,"\nRandom 0<k<n:\n", k)
    K1, S1 = sendKey(k, d, e1, n1, n)
    C = enc(M,e,n)
    K = getKey(K1,S1, d1,n1,e,n)
    D = dec(C, d, n)
    print("="*40)
    print("[***]Result:\nCipherText:", C, "\nClearText:", D)
    print("="*40)
    print("[***]Cheks:\nMessage:", M==D, "\nKey:", k==dec(K1, d1,n1))