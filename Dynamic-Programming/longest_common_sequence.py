P = "BATD"
Q = "ABACD"

# Naive approach


def naiveLCS(p, q):
    # Base case:
    if p == -1 or q == -1:
        return 0
    elif P[p] == Q[q]:
        return 1 + naiveLCS(p - 1, q - 1)
    elif P[p] != Q[q]:
        return max(naiveLCS(p - 1, q), naiveLCS(p, q - 1))


print("Size of the longest common sequence naive: ",
      naiveLCS(len(P) - 1, len(Q) - 1))


# Dynamic programming
res = [[-1] * len(Q) for _ in range(len(P))]


def LCS(p, q):
    # Base case
    if p == -1 or q == -1:
        res[p][q] = 0
    # Already seen case
    if res[p][q] != -1:
        return res[p][q]
    # Recusive calls
    elif P[p] == Q[q]:
        res[p][q] = 1 + LCS(p - 1, q - 1)
    elif P[p] != Q[q]:
        res[p][q] = max(LCS(p - 1, q), LCS(p, q - 1))
    return res[p][q]


print("Size of the longest common sequence: ",
      LCS(len(P) - 1, len(Q) - 1))


# Bottom up
def bottomUpLCS(str1, str2):
    # Adding dummy values
    P = "0" + str1
    Q = "0" + str2

    # 1 slot for each possible couple of parameter
    res = [[0] * len(Q) for _ in range(len(P))]

    for p in range(1, len(P)):  # start at 1 to skip dummy value
        for q in range(1, len(Q)):
            if P[p] == Q[q]:
                res[p][q] = 1 + res[p - 1][q - 1]
            elif P[p] != Q[q]:
                res[p][q] = max(res[p][q - 1], res[p - 1][q])

    return res[-1][-1]


print("Size of the longest common sequence bottom up: ",
      bottomUpLCS(P, Q))


# Backtracking
def backtrack(p, q):
    if p == -1 or q == -1:
        return ""

    elif P[p] == Q[q]:
        return backtrack(p - 1, q - 1) + P[p]

    elif res[p - 1][q] > res[p][q - 1]:
        return backtrack(p - 1, q)
    else:
        return backtrack(p, q - 1)


print("Biggest subsequence (backtracking): ",
      backtrack(len(P) - 1, len(Q) - 1))

# Directly Saving the sequence


P = "MZJAWXU"
Q = "XMJYAUZ"


def resultLCS(str1, str2):
     # Adding dummy values
    P = "0" + str1
    Q = "0" + str2

    res = [[""] * len(Q) for _ in range(len(P))]
    for p in range(1, len(P)):
        for q in range(1, len(Q)):
            if P[p] == Q[q]:
                res[p][q] = res[p - 1][q - 1] + P[p]
            elif P[p] != Q[q]:
                if len(res[p - 1][q]) > len(res[p][q - 1]):
                    res[p][q] = res[p - 1][q]
                else:
                    res[p][q] = res[p][q - 1]

    return res[-1][-1]


print("Longest common sequence: ", resultLCS(P, Q))
