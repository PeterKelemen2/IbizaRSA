import math
import random
import hashlib


def dec2bin(x):  # Tízes számrendszerből kettesbe váltás

    felso_korlat = int(math.log2(x)) + 1
    ret = []
    for i in range(felso_korlat + 1):
        if x & 2 ** i > 0:
            ret.append(i)
    return ret # 2 hatványait visszaadjuk mint tömb


def gyorsHatvany(a, exp, m):
    osszeg_l = dec2bin(exp)
    szorzat = a % m
    eredmeny = 1
    for i in range(max(osszeg_l) + 1):
        if i in osszeg_l:
            eredmeny = eredmeny * szorzat % m
        szorzat = szorzat ** 2 % m

    return eredmeny


print("Gyors ", gyorsHatvany(6, 297297297297297297297297297297297297297297297297297297297297297297297297, 103))

# print("Lassú ", 6**297297297297297297297297297297297297297297297297297297297297297297297297 % 103)

def modulus(a, x, m):
    return gyorsHatvany(a, x, m)


def keyGen(p, q):
    n = p * q
    fn = (p - 1) * (q - 1)
    while True:
        e = random.randint(2, fn - 1)
        if math.gcd(e, fn) == 1:
            break
    d = pow(e, -1, fn)
    return e, d, n, fn


def enc(m, e, n):
    return modulus(m, e, n)


def dec(c, d, n):
    return modulus(c, d, n)  # technikailag ugyanaz mint az enc, ezt csak formalitás miatt szedjük külön, mert az enc és
    # dec eltérhet attól függően, hogy szimmetrikus vagy asszimmetrikus titkosítást használunk


def sign(m, d, n):
    hsh = hashlib.sha3_256(m.to_bytes(4, "big"))
    sign_hsh = []
    for hsh_k in hsh.hexdigest():
        sign_hsh.append(enc(ord(hsh_k), d, n))  # az ord() visszaadja a karakter ASCII tábla szerinti értékét
    return sign_hsh


p = 773
q = 1709
e, d, n, fn = keyGen(p, q)
print(e, d, fn)
m = 1234
s = sign(m, d, n)
c = enc(m, e, n)
print("A nyilt uzenetem: ", m, " amely titkositva: ", c)
m_d = dec(c, d, n)
print("A titkositott uzenetem: ", c, " amely visszafejtve ", m_d)

# Hashelés és kiíratása
hashelendo = "almafa"
hashlib.sha3_256(hashelendo.encode("utf-8")).hexdigest()
print("Hashelendő: ", hashelendo)
print("Titkosított üzenet: ", hashlib.sha3_256(hashelendo.encode("utf-8")).hexdigest())
# a hashelés egy byte sorozatot kér bemenetként, ezért a
# szöveget lebontjuk utf-8 kódolású byte array-jé
