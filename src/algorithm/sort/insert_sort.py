#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     :2024/4/11 12:52
# @Author   :Hanjiang Chen
# @Email    :chen_han_jiang@163.com
# @Project  :structure_and_algorithm 
# @File     :insert_sort.py
# @Software :PyCharm
from typing import List


def insert_sort(arr: List) -> List:
    """
    插入排序：每一轮从未排序区间中选择基准元素，插入到已排序区间的合适位置
    """
    n = len(arr)
    for i in range(1, n):
        base = arr[i]
        p = i - 1  # 记录插入位置
        # 内循环,找出插入位置
        while p >= 0 and arr[p] > base:
            # 后移一位
            arr[p + 1] = arr[p]
            p -= 1
        arr[p + 1] = base

    return arr


if __name__ == '__main__':
    arr = [4, 6, 3, 8, 20, 2, 9]
    arr = insert_sort(arr)
    print("插入排序后的结果:", arr)
