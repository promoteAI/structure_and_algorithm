"""
数组
File: array.py
Author: Hanjiang Chen
email:chen_han_jiang@163.com
"""

import random
from typing import List


def random_access(nums: List[int]) -> int:
    '''随机访问元素'''
    # 在区间[0,len(nums)-1]随机抽取一个数
    random_idx = random.randint(0, len(nums) - 1)
    # 获取并返回元素
    random_num = nums[random_idx]
    return random_num


# 请注意，Python的list是动态数组，可以直接扩展
# 为了方便学习，本函数将 list 看作长度不可变的数组
def extend(nums: List[int], enlarge: int) -> List[int]:
    '''扩展数组长度'''
    # 初始化一个扩展长度后的数组
    res = [0] * (len(nums) + enlarge)
    # 将原数组元素复制到新数组
    for i in range(len(nums)):
        res[i] = nums[i]
    # 返回扩展后的数组
    return res


def insert(nums: List[int], num: int, index: int):
    '''在数组index索引处插入num'''
    # index及之后的所有元素向后移动一位
    for i in range(len(nums) - 1, index, -1):
        nums[i] = nums[i - 1]
    # num赋值给index处
    nums[index] = num


def remove(nums: List[int], index: int):
    '''删除索引index处的元素'''
    for i in range(index, len(nums) - 1):
        nums[i] = nums[i + 1]


def traverse(nums: List[int]):
    '''遍历数组'''
    cnt = 0
    # 通过索引遍历
    for i in range(len(nums)):
        cnt += nums[i]
    # 直接遍历
    for num in nums:
        cnt += num
    # 同时遍历索引和元素
    for idx, num in enumerate(nums):
        cnt += num
        cnt += nums[i]


def find(nums: List[int], target: int) -> int:
    '''查找指定元素'''
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1


if __name__ == '__main__':
    # 初始化arr
    arr = [0] * 5
    print(arr)
    nums = [1, 3, 5, 4, 2]
    print(nums)
    # 随机访问
    random_num = random_access(nums)
    print(random_num)
    # 长度扩展
    nums = extend(nums, 3)
    print(nums)
    # 插入元素
    insert(nums, 100, 3)
    print(nums)
    # 删除元素
    remove(nums, 4)
    print(nums)
    traverse(nums)
    # 查找元素
    print(find(nums,5))
