def counting_sort(array, maxval):
    """in-place counting sort
       O(n + maxval)"""
    m = maxval + 1
    # count the occurence of every possible value
    count = [0] * m  # /!\
    for a in array:
        count[a] += 1
    i = 0
    for a in range(m):
        for _ in range(count[a]):
            array[i] = a
            i += 1
    return array


print(counting_sort([1, 4, 7, 2, 1, 3, 2, 1, 4, 2, 3, 2, 1], 7))
