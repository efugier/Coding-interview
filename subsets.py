#-- Print or count all the subsets of a set


def subsets(A):  # O(2^n * n)
    res = [[]]
    for item in A:
        n = len(res)
        for i in range(n):
            res.append(res[i] + [item])  # O(n)

    return res


A = [1, 2, 3]
subs = subsets(A)
print(subs)
print(len(subs), " = ", 2**len(A))


def recSubsets(A, subset, i):
    if i < len(A):
        subset[i] = A[i]
        recSubsets(A, subset, i + 1)  # With our item
        subset[i] = None
        recSubsets(A, subset, i + 1)  # Without
    else:
        printSet(subset)


def printSet(a_set):
    print("{ ", end='')
    for item in a_set:
        if item != None:
            print(item, end=' ')
    print("}")


A = [1, 2, 3]
recSubsets(A, [None] * len(A), 0)
