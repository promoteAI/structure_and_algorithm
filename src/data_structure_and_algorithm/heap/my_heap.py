"""
自定义实现堆,基于数组实现
File: my_heap.py
Author: Hanjiang Chen
email:chen_han_jiang@163.com
"""
import heapq
import sys
from pathlib import Path
from typing import List

sys.path.append(str(Path(__file__).parent.parent))
from modules import print_heap


class MaxHeap:
    """使用数组实现大顶堆"""

    def __init__(self, arr: List[int]):
        # 添加进堆
        self.max_heap = arr
        # 堆化除叶子结点的其他节点
        for i in range(self.parent(self.size() - 1), -1, -1):
            self.sift_down(i)

    def left(self, i: int) -> int:
        """获取左子节点的索引"""
        return 2 * i + 1

    def right(self, i: int) -> int:
        """获取右子节点的索引"""
        return 2 * i + 2

    def parent(self, i: int) -> int:
        """获取父节点的索引"""
        return (i - 1) // 2

    def swap(self, i: int, j: int):
        """交换元素"""
        self.max_heap[i], self.max_heap[j] = self.max_heap[j], self.max_heap[i]

    def is_empty(self) -> bool:
        """判断堆是否为空"""
        return not self.max_heap

    def size(self) -> int:
        return len(self.max_heap)

    def push(self, val: int):
        """插入元素"""
        # 添加节点
        self.max_heap.append(val)
        # 从底至顶堆化
        self.sift_up(self.size() - 1)

    def pop(self) -> int:
        """弹出堆顶元素"""
        if self.is_empty():
            raise IndexError("pop from an empty heap")
        # 交换堆顶和最后一个元素
        self.swap(0, self.size() - 1)
        # 删除最后一个元素
        peek = self.max_heap.pop()
        # 堆顶元素出堆后，从顶至底堆化
        self.sift_down(0)
        # 返回堆顶元素
        return peek

    def peek(self) -> int:
        """查看堆顶元素"""
        return self.max_heap[0]

    def sift_up(self, i: int):
        """从i开始,自底向顶堆化"""
        while True:
            # 获取节点i的父节点
            parent = self.parent(i)
            # 父节点索引越界，或节点无须修复，则停止堆化
            if parent < 0 or self.max_heap[i] <= self.max_heap[parent]:
                break

            # 交换当前元素和父节点
            self.swap(i, parent)

            # i 继续向上走
            i = parent

    def sift_down(self, i: int):
        """从i开始,自顶向下堆化"""
        while True:
            # 判断i,l,r中最大的节点，记为ma
            l, r, ma = self.left(i), self.right(i), i
            if l < self.size() and self.max_heap[l] > self.max_heap[ma]:
                ma = l

            if r < self.size() and self.max_heap[r] > self.max_heap[ma]:
                ma = r
            # 若 i最大,或l,r越界则停止堆化
            if ma == i:
                break

            # 交换元素
            self.swap(i, ma)

            # 继续下一轮循环
            i = ma

    def print(self):
        """打印堆（二叉树）"""
        print_heap(self.max_heap)


if __name__ == '__main__':
    # 从列表创建堆
    lst = [1, 3, 2, 5, 4, 6]
    max_heap = MaxHeap(lst)
    max_heap.print()

    # 获取堆顶元素
    peek = max_heap.peek()
    print(f"\n堆顶元素为 {peek}")

    # 元素入堆
    val = 7
    max_heap.push(val)
    print(f"\n元素 {val} 入堆后")
    max_heap.print()

    # 堆顶元素出堆
    peek = max_heap.pop()
    print(f"\n堆顶元素 {peek} 出堆后")
    max_heap.print()

    # 获取堆的大小
    size = max_heap.size()
    print("堆的大小：", size)
