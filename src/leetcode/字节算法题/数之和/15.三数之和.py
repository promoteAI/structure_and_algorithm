"""
给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。
示例 1：

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
解释：
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
注意，输出的顺序和三元组的顺序并不重要。
"""
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i>(len(nums)-3):
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1
            # 记录已经遍历过的三元组
            record = set()
            while left<right:
                if nums[i]+nums[left]+nums[right]==0:
                    if (nums[i],nums[left],nums[right]) not in record:
                        record.add((nums[i],nums[left],nums[right]))
                        res.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                elif nums[i]+nums[left]+nums[right]<0:
                    left+=1
                else:
                    right-=1
        return res

if __name__ == '__main__':
    nums = [2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10]
    res = Solution().threeSum(nums)
    print(res)