"""
自定义列表
File:list.py
Author: Hanjiang Chen
email:chen_han_jiang@163.com
"""
from typing import List


class MyList:
    """自定义列表类"""

    def __init__(self):
        self._capacity = 10  # 列表容量
        self._arr: List[int] = [0] * self._capacity  # 数组，存储列表元素
        self._size: int = 0  # 列表长度(当前元素数量)
        self._extend_rate = 2  # 每次列表扩容的倍数

    def size(self):
        return self._size

    def capacity(self):
        return self._capacity

    def get(self, idx):
        if idx < 0 or idx >= self._size:
            raise IndexError("Index out of range")
        return self._arr[idx]

    def set(self, num, idx):
        if idx < 0 or idx >= self._size:
            raise IndexError("Index out of range")
        self._arr[idx] = num

    def extend_capacity(self):
        '''扩容'''
        self._arr = self._arr + [0] * self._capacity * (self._extend_rate - 1)
        self._capacity = len(self._arr)

    def add(self, num):
        '''尾部添加元素'''
        if self.size() == self.capacity():
            self.extend_capacity()
        self._arr[self._size] = num
        self._size += 1

    def insert(self, num, idx):
        '''中间插入元素'''
        if idx < 0 or idx >= self._size:
            raise IndexError("Index out of range")
        # 元素超出容量时，触发扩容机制
        if self._size == self._capacity:
            self.extend_capacity()
        # 移动元素
        for i in range(self._size - 1, idx - 1, -1):
            self._arr[i + 1] = self._arr[i]
        self._arr[idx] = num
        # 更新数量
        self._size += 1

    def to_array(self) -> List[int]:
        """返回有效长度的列表"""
        return self._arr[: self._size]


if __name__ == '__main__':
    nums = MyList()
    # 尾部添加元素
    nums.add(3)
    nums.add(2)
    nums.add(4)
    nums.add(1)
    nums.add(5)
    print(nums._arr)
    # 中间插入元素
    nums.insert(100, 3)
    print(nums._arr)
    # 访问元素
    print(nums.get(3))
    # 更新元素
    nums.set(888, 2)
    print(nums._arr)
    # 测试扩容机制
    for i in range(10):
        # 在 i = 5 时，列表长度将超出列表容量，此时触发扩容机制
        nums.add(i)
    print(f"扩容后的列表 {nums.to_array()} ，容量 = {nums.capacity()} ，长度 = {nums.size()}")
