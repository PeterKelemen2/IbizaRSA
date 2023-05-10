from random import randint
from BovitettEuklid import Bovitett_Euklid
from GyorsHatvany import GyorsHatvany
from KinaiMaradék import Kinai_Maradek
from Miller_Rabin import Miller_Rabin


def RandomPrim():
    while True:
        p = randint(2, 100000000)
        q = randint(2, 100000000)
        if p != q and p % 2 != 0 and q % 2 != 0 and Miller_Rabin(2, p) and Miller_Rabin(2, q):
            return p, q


def KeyGen(phi):
    while True:
        e = randint(2, phi)
        # e= 65536
        (d, x, y) = Bovitett_Euklid(phi,e)
        if d == 1:
            if y < 1:
                y = y + phi
            return e, y # nyilvános, titkos kulcs


def RSA():
    # Generating the key
    p, q = RandomPrim()
    modulus = p * q
    phi = (p - 1) * (q - 1)
    e, d = KeyGen(phi)

    uzenet = 5
    print("Alap üzenet: " + str(uzenet))

    # Encryption
    c = GyorsHatvany(uzenet, e, modulus)
    print("Titkosított üzenet: " + str(c))

    # Decryption
    m = Kinai_Maradek(p, q, c, d) # két prím, titkosított üzenet, titkos kulcs
    print("Visszafejtett üzenet: " + str(m))

    # Signature
    S = Kinai_Maradek(p, q, uzenet, d)

    # Verifying
    if m == GyorsHatvany(S, e, modulus): # aláírás, nyilvános kulcs"adik"
        print("Megfelelő Aláírás")
    else:
        print("Nem megfelelő aláírás")


RSA()
