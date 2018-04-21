# -1 is a dummy value to start indexing at 1
W = [-1, 1, 2, 4, 2, 5]  # Weight, kg
V = [-1, 5, 3, 5, 3, 2]  # Value, $

items = [0, 0, 0, 0, 0]  # 1: item included, 0: no

CAPACITY = 10

#-- Naive version calculating several time the same thing recursive calls: O(2^n = 32)


def naiveKS(n, c):
    """ n is both the number of item left to sotre and the id the current item to store
        returns the maximum possible score """
    # Base case
    if n == 0 or c == 0:
        return 0

    # Recursive calls
    elif W[n] > c:
        return naiveKS(n - 1, c)
    else:
        tmp1 = naiveKS(n - 1, c)
        tmp2 = V[n] + naiveKS(n - 1, c - W[n])
        return max(tmp1, tmp2)


print("Naive one: ", naiveKS(5, CAPACITY))

#-- Same but storing the every intermediate result
res = [[-1] * CAPACITY for _ in range(len(V))]


def KS(n, c):
    """ returns the maximum possible score for an instance of size n adn capacity c """
    # Base case
    if n == 0 or c == 0:
        res[n][c] = 0
    # Already seen case
    elif res[n][c] != -1:
        return res[n][c]
    # Recursive calls
    elif W[n] > c:
        res[n][c] = KS(n - 1, c)
    else:
        tmp1 = KS(n - 1, c)
        tmp2 = V[n] + KS(n - 1, c - W[n])
        res[n][c] = max(tmp1, tmp2)

    return res[n][c]


print("Dynamic one: ", KS(len(V) - 1, CAPACITY - 1))
