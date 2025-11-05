from typing import List

# 动态规划：暴力解法
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        k = 1
        max = nums[0]
        while k<=n:
            for i in range(n):
                sub_arr = nums[i:i+k]
                if sum(sub_arr) > max:
                    max = sum(sub_arr)
            k+=1
        return max

# dp问题
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        pre = 0
        maxAns = nums[0]
        for i in range(n):
            pre = max(pre+nums[i],nums[i])
            maxAns = max(maxAns,pre)
        return maxAns