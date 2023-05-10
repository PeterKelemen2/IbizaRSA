from GyorsHatvany import GyorsHatvany


def Miller_Rabin(a, p):
    s = 1
    while ((p - 1) / pow(2, s)) % 2 != 1:
        s = s + 1
    d = (p - 1) / pow(2, s)

    if GyorsHatvany(a, d, p) == 1:
        return True
    else:
        if s == 1:
            if GyorsHatvany(a, d, p) == p - 1:
                return True
        else:
            for r in range(0, s - 1):
                if GyorsHatvany(a, d * pow(2, r), p) == p - 1:
                    return True
                elif GyorsHatvany(a, d * pow(2, r), p) == 1:
                    return False
        return False
