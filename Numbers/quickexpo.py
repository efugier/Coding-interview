def fastExpo(a, b, q):
    # a^b % q
    p2, ap2, res = 1, a % q, 1
    while b > 0:
        if p2 & b > 0:
            b -= p2
            res = (res * ap2) % q
        p2 *= 2
        ap2 = (ap2 * ap2) % q
    return res
