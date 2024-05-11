#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     :2024/5/11 23:05
# @Author   :Hanjiang Chen
# @Email    :chen_han_jiang@163.com
# @Project  :structure_and_algorithm 
# @File     :02_climb_stairs_dfs_mem.py
# @Software :PyCharm

"""
初识动态规划
爬楼梯问题：给定一个共有n阶的楼梯，你每步可以上1阶或者2阶，请问有多少种方案可以爬到楼顶？
"""
from typing import List


class Solution:
    def dfs(self, n: int, mem: List[int]):
        if n == 1 or n == 2:
            return n
        if mem[n] != 0:
            return mem[n]
        # 状态转移方程 # dp[i] = dp[i-1] + dp[i-2]
        cnt = self.dfs(n - 1, mem) + self.dfs(n - 2, mem)
        # 记录dp[i]
        mem[n] = cnt
        return cnt

    def climbStairs(self, n: int) -> int:
        # 引入额外存储，避免重复计算重叠子问题
        mem = [0] * (n + 1)
        cnt = self.dfs(n, mem)
        return cnt


if __name__ == '__main__':
    # 法三:记忆化搜素,重复子问题只计算一次
    n = 3
    res = Solution().climbStairs(n)
    print(f"爬{n}阶楼梯总的方案数量:{res}")
