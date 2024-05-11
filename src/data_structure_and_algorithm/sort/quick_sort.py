#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     :2024/4/11 14:07
# @Author   :Hanjiang Chen
# @Email    :chen_han_jiang@163.com
# @Project  :structure_and_algorithm 
# @File     :quick_sort.py
# @Software :PyCharm

from typing import List


def quick_sort(arr: List, l, r) -> List:
    """
    快速排序:
    """
    if l >= r:
        return
    # 划分哨兵
    pivot = partition(arr, l, r)
    # 递归左区间
    quick_sort(arr, l, pivot - 1)
    quick_sort(arr, pivot + 1, r)
    return arr


def partition(arr: List, l: int, r: int):
    """
    哨兵划分：选择数组中的某个元素作为“基准数”，将所有小于基准数的元素移到其左侧，而大于基准数的元素移到其右侧。
    """
    i = l
    j = r
    while i < j:
        # 从右到左找首个小于基准的元素
        while i < j and arr[j] >= arr[l]:
            j -= 1
        # 从左到右找首个大于基准的元素
        while i < j and arr[i] <= arr[l]:
            i += 1
        # 交换元素
        arr[i], arr[j] = arr[j], arr[i]
    # 将基准数交换至两子数组的分界线
    arr[i], arr[l] = arr[l], arr[i]
    # 返回基准数的索引
    return i


if __name__ == '__main__':
    arr = [5, 7, 9, 1, 4, 2, 6, 3, 11]
    arr = quick_sort(arr, 0, len(arr) - 1)
    print(arr)
