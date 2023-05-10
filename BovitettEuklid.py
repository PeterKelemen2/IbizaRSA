def Bovitett_Euklid(FirstNumber, SecondNumber):
    x0, x1, y0, y1 = 1, 0, 0, 1
    k = 0
    while SecondNumber != 0:
        remainder, quotient = FirstNumber % SecondNumber, FirstNumber // SecondNumber
        FirstNumber = SecondNumber
        SecondNumber = remainder
        x, y = x1, y1
        x1 = quotient * x1 + x0
        y1 = quotient * y1 + y0
        x0, y0 = x, y
        k += 1
    x = pow(-1, k) * x0
    y = pow(-1, k + 1) * y0
    d, x, y = FirstNumber, x, y
    return d, x, y

