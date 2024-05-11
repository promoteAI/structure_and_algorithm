#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     :2024/5/11 22:23
# @Author   :Hanjiang Chen
# @Email    :chen_han_jiang@163.com
# @Project  :structure_and_algorithm 
# @File     :01_climb_stairs.py
# @Software :PyCharm

"""
初识动态规划
爬楼梯问题：给定一个共有n阶的楼梯，你每步可以上1阶或者2阶，请问有多少种方案可以爬到楼顶？
"""
from typing import List


class Solution:
    def backtrack(self, state: int, choices: List[int], res: List[int], n: int):
        """回溯"""
        # 记录解
        if state == n:
            res[0] += 1
        # 遍历所有选择
        for choice in choices:
            # 剪枝
            if state + choice > n:
                continue
            # 做出选择，更新状态
            self.backtrack(state + choice, choices, res, n)
            # 回退

    def climbStairs(self, n: int) -> int:
        """法一:通过回溯穷举可能方案"""
        choices = [1, 2]  # 选择爬1阶或2阶
        state = 0  # 从0阶开始爬
        res = [0]  # 记录方案数
        self.backtrack(state, choices, res, n)
        return res[0]


if __name__ == '__main__':
    # 法一:回溯法
    n = 3
    res = Solution().climbStairs(n)
    print(f"爬{n}阶楼梯总的方案数量:{res}")
