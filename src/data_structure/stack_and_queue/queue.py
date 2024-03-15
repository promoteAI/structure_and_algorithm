"""
队列：先入先出
File: queue.py
Author: Hanjiang Chen
email:chen_han_jiang@163.com
"""
from typing import List
from collections import deque

if __name__ == '__main__':
    # 初始化队列
    # 在python中，一般将双向队列类deque作为队列使用
    # 虽然queue.Queue()是纯正的队列类，但不好使用
    queue = deque()
    print("空队列:",queue)
    # 元素入队
    queue.append(1)
    queue.append(2)
    queue.append(5)
    queue.append(4)
    queue.append(3)
    print("队列 queue=", queue)
    # 访问队首元素
    front=queue[0]
    print("队首元素:",front)
    # 元素出队
    pop=queue.popleft()
    print("出队元素:",pop)
    # 获取队列长度
    size=len(queue)
    print("队列长度:",size)
    # 判断队列是否为空
    is_empty=len(queue)==0
    print("队列是否为空:",is_empty)

