#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     :2024/5/11 23:29
# @Author   :Hanjiang Chen
# @Email    :chen_han_jiang@163.com
# @Project  :structure_and_algorithm 
# @File     :04_climb_stairs_dp.py
# @Software :PyCharm
"""
初识动态规划
爬楼梯问题：给定一个共有n阶的楼梯，你每步可以上1阶或者2阶，请问有多少种方案可以爬到楼顶？
"""
from typing import List


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        # 初始化 dp 表，用于存储子问题的解
        dp = [0] * (n + 1)
        # 初始状态
        dp[1], dp[2] = 1, 2
        # 状态转移：从较小子问题逐步求解较大子问题
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

    def climbStairs_comp(self, n: int) -> int:
        """空间优化,在动态规划问题中，当前状态往往仅与前面有限个状态有关，
        这时我们可以只保留必要的状态，通过“降维”来节省内存空间。这种空间优化技巧被称为“滚动变量”或“滚动数组”。"""
        if n == 1 or n == 2:
            return n
        a, b = 1, 2
        # 状态转移：从较小子问题逐步求解较大子问题
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b


if __name__ == '__main__':
    # 法四:动态规划,是一种“从底至顶”的方法,从最小子问题的解开始，迭代地构建更大子问题的解，直至得到原问题的解。
    n = 3
    res = Solution().climbStairs(n)
    print(f"爬{n}阶楼梯总的方案数量:{res}")
