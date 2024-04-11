#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     :2024/4/11 11:19
# @Author   :Hanjiang Chen
# @Email    :chen_han_jiang@163.com
# @Project  :structure_and_algorithm 
# @File     :bubble_sort.py
# @Software :PyCharm


from typing import List


def bubble_sort(arr: List) -> List:
    """
    冒泡排序：
        从数组最左端开始向右遍历，依次比较相邻元素大小，如果“左元素 > 右元素”就交换二者。遍历完成后，最大的元素会被移动到数组的最右端。
    """
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == '__main__':
    arr = [5, 3, 8, 1, 7, 2, 9]
    arr = bubble_sort(arr)
    print(arr)
