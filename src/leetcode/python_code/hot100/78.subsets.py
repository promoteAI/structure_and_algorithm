#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     :2024/4/26 10:37
# @Author   :Hanjiang Chen
# @Email    :chen_han_jiang@163.com
# @Project  :structure_and_algorithm 
# @File     :78.subsets.py
# @Software :PyCharm

from typing import List


class Solution:

    def back_track(self, start: int, state:List[int],choices: List[int], res: List[List[int]]):
        # 记录解
        res.append(list(state))
        # 从start遍历所有选择
        for i in range(start, len(choices)):
            # 尝试选择,更新状态
            state.append(choices[i])
            # 进行下一轮选择
            self.back_track(i+1,state, choices, res)
            # 回退
            state.pop()

    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
        解集 不能 包含重复的子集。可以按 任意顺序 返回解集。
        """
        res = []
        # 回溯
        self.back_track(start=0, state=[],choices=nums, res=res)
        return res


if __name__ == '__main__':
    nums = [1, 2, 3]
    # nums = [0]
    # 输出：[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    res = Solution().subsets(nums)
    print(res)
