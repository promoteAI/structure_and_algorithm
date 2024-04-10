#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     :2024/4/10 15:28
# @Author   :Hanjiang Chen
# @Email    :chen_han_jiang@163.com
# @Project  :structure_and_algorithm 
# @File     :binary_search_insert.py
# @Software :PyCharm
from typing import List


# 搜索元素的插入位置
def binary_search_insert_simple(arr: List, target: int) -> int:
    """
    简单情况:列表中无重复元素
    """
    l = 0
    r = len(arr) - 1
    while l <= r:
        m = (l + r) // 2
        if arr[m] > target:
            r = m - 1
        elif arr[m] < target:
            l = m + 1
        else:
            return m
    return l


def binary_search_insert(arr: List, target: int) -> int:
    """
    复杂情况:列表中有重复元素
    """
    l = 0
    r = len(arr) - 1
    while l <= r:
        m = (l + r) // 2
        if arr[m] > target:
            r = m - 1
        elif arr[m] < target:
            l = m + 1
        else:
            # 此时无法确定m位置的左右是否还有target元素,进行线性遍历找到最左面的target的索引
            # for k in range(m, -1, -1):
            #     if arr[k] != target:
            #         return k + 1
            r = m - 1
    return l


if __name__ == '__main__':
    # 无重复元素
    arr = [1, 3, 4, 6, 9, 13, 17, 23]
    target = 9
    insert_i = binary_search_insert_simple(arr, target)
    print("目标元素插入列表的位置:", insert_i)
    # 插入
    arr.insert(insert_i, target)
    print(f"插入{target}后的列表:", arr)
    # 有重复元素
    arr = [1, 3, 4, 4, 4, 6, 9, 9, 9, 9, 13, 17, 23]
    target = 4
    insert_i = binary_search_insert(arr, target)
    print("目标元素插入列表的位置:", insert_i)
    # 插入
    arr.insert(insert_i, target)
    print(f"插入{target}后的列表:", arr)
