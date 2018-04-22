#- find a,b,c so that a + b + c = 0


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        dic, pos, neg = {}, [], []
        for v in nums:
            if v not in dic:
                dic[v] = 0
                if v > 0:
                    pos.append(v)
                elif v < 0:
                    neg.append(v)
            dic[v] += 1

        if 0 in dic and dic[0] > 2:
            res = [[0, 0, 0]]
        else:
            res = []

        for p in pos:
            for n in neg:
                o = -(p + n)  # for opposite
                if o in dic:
                    if o == p and dic[p] > 1:
                        res.append([n, p, p])
                    elif o == n and dic[n] > 1:
                        res.append([n, n, p])
                    elif o < n or o > p or o == 0:
                        res.append([n, o, p])

        return res
