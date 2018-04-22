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
                o = -(p + n)  # o for opposite
                if o in dic:
                    if o == p and dic[p] > 1:
                        res.append([n, p, p])
                    elif o == n and dic[n] > 1:
                        res.append([n, n, p])
                    elif o < n or o > p or o == 0:
                        res.append([n, o, p])

        return res

    def threeSum2(self, nums):
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if not(i == 0 or nums[i] > nums[i - 1]):
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1

        return res
