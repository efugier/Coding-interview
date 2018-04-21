#-- Clean merge sort


# Recursive

def merge(t, i, j, k, aux):
    # merge t[i:k] in aux[i:k] supposing t[i:j] and t[j:k] are sorted
    a, b = i, j  # iterators
    for s in range(i, k):
        if a == j or (b < k and t[b] < t[a]):
            aux[s] = t[b]
            b += 1
        else:
            aux[s] = t[a]
            a += 1


def merge_sort(t):
    aux = [None] * len(t)

    def merge_rec(i, k):
        # merge sort t from i to k
        if k > i + 1:
            j = i + (k - i) // 2
            merge_rec(i, j)
            merge_rec(j, k)
            merge(t, i, j, k, aux)
            t[i:k] = aux[i:k]
    merge_rec(0, len(t))


# Iterative, O(1) in space but worse time complexity
# merge subarrays of size s^k for every k so that s**k < n
def merge_sort_ite(t):
    s = 1
    while s <= len(t):
        for i in range(0, len(t), s * 2):
            left, right = i, min(len(t), i + 2 * s)
            mid = i + s
            # merge t[i:i + 2 * s]
            p, q = left, mid
            while p < mid and q < right:
                if t[p] > t[q]:
                    tmp = t[q]
                    t[p + 1: q + 1] = t[p:q]  # /!\ O(n)
                    t[p] = tmp
                    mid += 1
                    q += 1
                p += 1
        s *= 2

    return t


tab = [172, 4784, 4, 623, 8, 2, 63, 9479, 42, 98]
merge_sort_ite(tab)

print(tab)
