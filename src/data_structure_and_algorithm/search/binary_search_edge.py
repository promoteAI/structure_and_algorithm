#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     :2024/4/10 16:04
# @Author   :Hanjiang Chen
# @Email    :chen_han_jiang@163.com
# @Project  :structure_and_algorithm 
# @File     :binary_search_edge.py
# @Software :PyCharm

# 二分查找边界

from typing import List
from binary_search_insert import binary_search_insert

def binary_search_left_edge(arr:List,target:int)->int:
    """查找左边界"""
    i=binary_search_insert(arr,target)
    if i==len(arr) or arr[i]!=target:
        return -1
    return i

def binary_search_right_edge(arr:List,target:int)->int:
    """查找右边界"""
    i=binary_search_insert(arr,target+1)
    j=i-1
    if j==-1 or arr[j]!=target:
        return -1
    return j

if __name__ == '__main__':
    arr=[1,4,6,8,8,8,13,13,17,23]
    target=7
    i=binary_search_left_edge(arr,target)
    print("左边界索引:",i)
    arr=[1,4,6,8,8,8,13,13,17,23]
    target=8
    i=binary_search_right_edge(arr,target)
    print("右边界索引:",i)
