from GyorsHatvany import GyorsHatvany
from BovitettEuklid import Bovitett_Euklid


def Kinai_Maradek(p, q, c, d):
    c1 = GyorsHatvany(c, d % (p - 1), p)
    c2 = GyorsHatvany(c, d % (q - 1), q)
    M1, M2 = q, p
    M = p * q

    d, y1, y2 = Bovitett_Euklid(M1, M2)

    return ((c1 * y1 * M1) + (c2 * y2 * M2)) % M
