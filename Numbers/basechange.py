def basebTo10(x, b=2):  # Horner scheme
    u = 0
    for a in x:
        u = b * u + int(a)
    return u


def base10Tob(q, b=2):
    s = ''
    while q > 0:
        q, r = divmod(q, b)
        s = str(r) + s
    return s


#-- When there is no 0 in our base
def base10tobNoZero(q, b=2):
    s = ''
    while q > 0 or not s:
        q, r = divmod(q - 1, b)  # -1 to remove 0
        s = chr(65 + r) + s
    return s


print(base10Tob(10))
print(basebTo10(base10Tob(10)))
print(base10Tob(basebTo10(str(10))))
print(base10tobNoZero(52, 26))
