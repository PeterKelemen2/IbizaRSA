def GyorsHatvany(alap, exp, mod):
    alap = alap % mod
    if exp == 0:
        return 1
    elif exp == 1:
        return alap
    elif exp % 2 == 0:
        return GyorsHatvany(alap * alap % mod, exp / 2, mod)
    else:
        return alap * GyorsHatvany(alap, exp - 1, mod) % mod

def toBinary(x):
    BinString = ""
    while x != 0:
        BinString += str(x % 2)
        x = x // 2
    return BinString
