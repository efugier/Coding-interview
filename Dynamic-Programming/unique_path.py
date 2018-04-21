#-- Unique paths on a grid when only moving down or right

# Classic Dynamic programming


def uniquePaths3(n, m):
    sol = [[1] * m for _ in range(n)]
    for i in range(1, n):
        for j in range(1, m):
            sol[i][j] = sol[i - 1][j] + sol[i][j - 1]
    return sol[-1][-1]


# Augmented Dynamic Programming
def uniquePaths2(n, m):
    sol = [1] * m
    for _ in range(1, n):
        for i in range(1, m):
            sol[i] += sol[i - 1]
    return sol[-1]


# Combinatory
def uniquePaths(n, m):
    return binom(n + m - 2, m - 1)


def binom(n, k):
    res = 1
    for i in range(k):
        res *= n - i
        res //= i + 1
    return res
