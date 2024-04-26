#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     :2024/4/25 17:09
# @Author   :Hanjiang Chen
# @Email    :chen_han_jiang@163.com
# @Project  :structure_and_algorithm 
# @File     :46.permute.py
# @Software :PyCharm

from typing import List


# 全排列

class Solution:

    def back_track(self, stat: List[int], choices: List[int], selected: List[bool], res: List[List[int]]):
        """
        :param stat:
        :param choices:
        :param selected:
        :param res:
        :return:
        """
        # 记录解
        if len(stat) == len(choices):
            res.append(list(stat))
            return
        # 遍历所有选择
        for i, choice in enumerate(choices):
            # 剪枝:不选择重复元素
            if not selected[i]:
                # 尝试:做出选择，更新状态
                selected[i] = True
                stat.append(choice)
                # 进行下一轮选择
                self.back_track(stat=stat,choices=choices,selected=selected,res=res)
                # 回退
                selected[i]=False
                stat.pop()

    def permute(self, nums: List[int]) -> List[List[int]]:
        """给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。"""
        res = []  # 记录最终解
        # 回溯算法
        self.back_track(stat=[], choices=nums, selected=[False]*len(nums), res=res)
        return res


if __name__ == '__main__':
    nums = [1, 2, 3]
    # [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    res = Solution().permute(nums=nums)
    print(res)
