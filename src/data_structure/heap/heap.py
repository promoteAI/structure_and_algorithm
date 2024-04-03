"""
堆
File: heap.py
Author: Hanjiang Chen
email:chen_han_jiang@163.com
"""
import heapq
import sys
from pathlib import Path
from typing import List

sys.path.append(str(Path(__file__).parent.parent))
from modules import TreeNode, print_tree, list_to_tree, tree_to_list

if __name__ == '__main__':
    # 初始化小顶堆
    min_heap, flag = [], 1
    max_heap, flag = [], -1
    # python 的heapq模块默认实现小顶堆
    # 考虑将“元素取负”后再入堆，这样就可以将大小关系颠倒，从而实现大顶堆
    #  在本示例中，flag = 1 时对应小顶堆，flag = -1 时对应大顶堆
    heapq.heappush(max_heap, flag * 1)
    heapq.heappush(max_heap, flag * 2)
    heapq.heappush(max_heap, flag * 6)
    heapq.heappush(max_heap, flag * 4)
    heapq.heappush(max_heap, flag * 3)
    heapq.heappush(max_heap, flag * 5)

    # 获取堆顶元素
    peek = flag * max_heap[0]
    print("堆顶元素:", peek)

    # 获取堆的大小
    size = len(max_heap)
    print("堆的大小:", size)

    # 堆顶元素出堆
    res = []
    for _ in range(len(max_heap)):
        res.append(flag * heapq.heappop(max_heap))
    print("元素出堆顺序:", res)

    # 判断元素是否为空
    print("堆是否为空:", max_heap == [])
    print("堆是否为空:", not max_heap)

    # 从列表创建堆
    min_heap = [1, 2, 6, 4, 5, 3]
    heapq.heapify(min_heap)
    print("从列表创建堆:", min_heap)
