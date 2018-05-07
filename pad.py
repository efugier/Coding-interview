def combinationSum4(nums, target):
    # number of ways to sum sum of the
    #
    n, dp = 1, [1]
    # nums.sort()
    while n <= target:
        ans = 0
        for i in nums:
            if i > n:
                break
            ans += dp[n - i]  # number of ways to sum to n ending with i
        print("end of loop:", ans, dp[n - 1])
        dp.append(ans)
        n += 1
    print(dp)
    return dp[target]


def sumTo(target):  # if nums = [1, 2, ..., target-1]
    return (1 << target - 1) - 1


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        dic = {}
        for v in nums:
            if v in dic:
                dic[v] += 1
            else:
                dic[v] = 1
        used_numbers = set()
        for i, vi in enumerate(nums, 1):
            j = i
            while j < len(nums):
                if (- vi - nums[j] in dic and not (vi in used_numbers and nums[j] in used_numbers) 
                    and dic[vi] - (vi == nums[j]) - (vi == -vi - nums[j]) > 0 
                    and dic[nums[j]] - (nums[j] == vi) - (nums[j] == -vi - nums[j]) > 0):
                    res.append([vi, nums[j], -vi - nums[j]])
                    used_numbers.add(vi)
                    used_numbers.add(nums[j])
                    used_numbers.add(-vi -nums[j])
                j += 1
        return res


"""
Let $$c_n$$ be the number of ways to make $$n$$ using a set of number $$S$$. 

* The number of ways to make $$n$$ is the sum of the number of ways to make $$n$$ ending with $$i$$ for every $$i \in S$$.
* The number of ways to make $$n$$ ending with $$i$$ is $$c_{n-i}$$ (just sum up to $$n-i$$ then add $$i$$).

In short, this sums up (pun intended) to:
$$
c_n = \sum_{i \in S}{c_{n-i}}
$$

which in python is:
``` python
def combinationSum4(nums, target):
    n, dp = 1, [1]
    nums.sort()
    while n <= target:
        ans = 0
        for i in nums:
            if i > n: break
            ans += dp[n - i]
        dp.append(ans)
        n += 1
            
    return dp[target]
```

As a side note, if $$S = {1, 2, ..., n-1}$$ then $$c_n = 2^{n-1}-1$$, which is the $$(n-1)^{th}$$ Mercenne number.

In python this would look like this:
```python
def sumTo(target):  # if nums = [1, ... target-1]
    return (1 << target - 1) - 1
```
"""
