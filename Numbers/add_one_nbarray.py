
def addOne(l):
    # Treat the array l as a number
    i = len(l) - 1
    while i >= 0:
        if l[i] < 9:
            l[i] += 1
            break
        i -= 1
    else:
        l.append(0)
        for j in range(len(l) - 1):
            l[j] = 0
        l[0] = 1


nb = []
for k in range(10):
    addOne(nb)
    print(nb)
