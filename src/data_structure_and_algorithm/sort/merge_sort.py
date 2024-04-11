#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     :2024/4/11 15:02
# @Author   :Hanjiang Chen
# @Email    :chen_han_jiang@163.com
# @Project  :structure_and_algorithm 
# @File     :merge_sort.py
# @Software :PyCharm
from typing import List


def merge_sort(arr: List, l: int, r: int):
    """
    归并排序:分为划分与合并阶段
    """
    # 递归终止条件
    if l >= r:
        return
    # 计算中间索引
    mid = (l + r) // 2
    # 递归划分左子区间
    merge_sort(arr, l, mid)
    # 递归划分右子区间
    merge_sort(arr, mid + 1, r)
    # 合并阶段
    merge(arr, l, mid, r)
    return arr


def merge(arr: List, l: int, mid: int, r: int):
    """
    合并左子数组[l,mid]和右子数组[mid+1,r],左右子数组均为有序数组，需要额外临时存储
    """
    # 创建临时数组保存合并的结果
    temp = [0] * (r - l + 1)
    # 初始化左子数组和右子数组的起始索引
    i, j, k = l, mid + 1, 0

    # 当左右子数组都还有元素时，进行比较并将较小的元素复制到临时数组中
    while i <= mid and j <= r:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        # 临时数组索引+1
        k += 1

    # 将左子数组剩余元素复制到临时数组
    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1
    # 将右子数组剩余元素复制到临时数组
    while j <= r:
        temp[k] = arr[j]
        j += 1
        k += 1
    # 将临时数组复制到原数组对应区间
    for k in range(len(temp)):
        arr[l + k] = temp[k]


if __name__ == '__main__':
    arr = [5, 3, 6, 7, 1, 4, 9, 8]
    arr = merge_sort(arr, 0, len(arr) - 1)
    print(arr)
