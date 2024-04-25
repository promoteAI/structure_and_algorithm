#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     :2024/4/25 15:32
# @Author   :Hanjiang Chen
# @Email    :chen_han_jiang@163.com
# @Project  :leetcode 
# @File     :topK.py
# @Software :PyCharm
import heapq
from typing import List

def topK(nums: List,k:int):
    """给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。"""
    heap=[-x for x in nums]
    # 堆化数组
    heapq.heapify(heap)
    print(heap)
    # 弹出k-1个堆顶元素
    for _ in range(k-1):
        heapq.heappop(heap)
    # 返回第k个最大元素
    return -heapq.heappop(heap)

if __name__ == '__main__':
    test_1, k_1 = [3, 2, 1, 5, 6, 4], 2
    test_2, k_2 = [3, 2, 3, 1, 2, 4, 5, 5, 6], 3
    res = topK(nums=test_2, k=k_2)
    print(res)
