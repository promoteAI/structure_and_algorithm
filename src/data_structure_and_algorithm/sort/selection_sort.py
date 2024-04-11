#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     :2024/4/11 10:10
# @Author   :Hanjiang Chen
# @Email    :chen_han_jiang@163.com
# @Project  :structure_and_algorithm 
# @File     :selection_sort.py
# @Software :PyCharm

from typing import List


def selection_sort(arr: List) -> List:
    """
    选择排序：每次从未排序区间中选择最大或最小的元素和已排序区间的末尾元素交换
    """
    n = len(arr)
    for i in range(n - 1):
        # 内循环找到未排序最小的元素
        k = i
        for j in range(i, n):
            if arr[j] < arr[k]:
                k = j
        # 交换已排序中尾元素和未排序中最小的元素
        arr[i], arr[k] = arr[k], arr[i]
    return arr


if __name__ == '__main__':
    arr = [2, 5, 4, 9, 7, 11]
    arr = selection_sort(arr)
    print(arr)
