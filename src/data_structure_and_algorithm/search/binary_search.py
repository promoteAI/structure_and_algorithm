#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     :2024/4/10 10:46
# @Author   :Hanjiang Chen
# @Email    :chen_han_jiang@163.com
# @Project  :structure_and_algorithm 
# @File     :binary_search.py
# @Software :PyCharm

from typing import List


def binary_search(arr: List[int], target: int) -> int:
    """
    二分查找(双闭区间)
    """
    l = 0
    r = len(arr) - 1
    while l <= r:
        # 每次重新计算中心索引
        m = (l + r) // 2
        if arr[m] > target:  # 中间元素比目标值大,说明target在左子区间
            # 移动右指针
            r = m - 1
        elif arr[m] < target:  # 中间元素比目标值小,说明target在右子区间
            # 移动左指针
            l = m + 1
        else:
            return m

    return -1


if __name__ == '__main__':
    arr = [1, 3, 6, 8, 12, 15, 17, 23, 26, 34, 39]
    target = 15
    elment_i = binary_search(arr, target)
    print("目标元素在有序列表中的索引为:", elment_i)
