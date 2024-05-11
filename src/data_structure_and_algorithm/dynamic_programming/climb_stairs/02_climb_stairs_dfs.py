#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     :2024/5/11 23:05
# @Author   :Hanjiang Chen
# @Email    :chen_han_jiang@163.com
# @Project  :structure_and_algorithm 
# @File     :02_climb_stairs_dfs.py
# @Software :PyCharm

"""
初识动态规划
爬楼梯问题：给定一个共有n阶的楼梯，你每步可以上1阶或者2阶，请问有多少种方案可以爬到楼顶？
"""
from typing import List


class Solution:
    def dfs(self, n: int):
        if n == 1 or n == 2:
            return n
        # 状态转移方程
        cnt = self.dfs(n - 1) + self.dfs(n - 2)
        return cnt

    def climbStairs(self, n: int) -> int:
        cnt = self.dfs(n)
        return cnt


if __name__ == '__main__':
    # 法二:暴力搜索:问题分解的角度分析
    n = 3
    res = Solution().climbStairs(n)
    print(f"爬{n}阶楼梯总的方案数量:{res}")
