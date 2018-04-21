def efficientCombination(nb_occ_list):
    # number of ways permutations of n items
    # considering (1, 2) != (2, 1)
    # nb_occ_list[i] is the number of times the item i is in the set
    res = 1
    n = sum(nb_occ_list)
    i = 0
    for nb_occ in nb_occ_list:
        for ni in range(1, nb_occ + 1):
            res *= n - i
            res //= ni
            i += 1
    return res


print(efficientCombination([1, 2]))
