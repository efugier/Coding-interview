#-- Rotate left an array in place


def rotate_left(list_numbers, k):
    n = len(list_numbers)
    k %= n
    # reverse the whole list
    reverse(list_numbers, 0, n - 1)
    # put the last element on spot k (i.e. where it belongs now) and restore the order before it
    reverse(list_numbers, 0, n - k - 1)
    # restore the order after it
    reverse(list_numbers, n - k, n - 1)
    return list_numbers


def reverse(l, i, j):
    for k in range((j - i) // 2 + 1):
        l[i + k], l[j - k] = l[j - k], l[i + k]
