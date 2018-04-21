# Kadane's algorithm
#
# every subarray has an ending
# the maximum subarray ending at the spot i + 1 is either
#   1) maximum subarray ending at the spot i + [i + 1]
#   2) [i + 1]
#
# The maximum subarray is the best subarray that in one of the array's spots


def maxSum(A):
    current_sum = A[0]
    max_sum = A[0]
    for v in A:
        current_sum = max(v, v + current_sum)

        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum


def maxSubArray(A):
    max_start, max_end = 0, 0
    max_sum = A[0]

    current_start, current_sum = 0, A[0]

    for i, v in enumerate(A):
        if current_sum > 0:
            current_sum += v
        else:
            current_start = i
            current_sum = v

        if current_sum > max_sum:
            max_sum = current_sum
            max_start = current_start
            max_end = i

    return max_start, max_end, max_sum


array = [1, 2, -3, 5, 6, -3, 4]

print(maxSum(array))
print(maxSubArray(array))
