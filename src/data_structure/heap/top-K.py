"""
获取最大的K个元素
File: top-K.py
Author: Hanjiang Chen
email:chen_han_jiang@163.com
解决思路:
    1.每次获取最大的元素，然后删除该元素，直到获取到K个元素为止。
    2.排序后，获取最大的K个元素。
    3.使用堆，每次获取堆顶的元素，然后删除该元素，直到获取到K个元素为止。
"""
import heapq


def get_top_k(nums, k):
    """
    1.初始化一个小堆顶
    2.将数组前k个元素入堆
    3.从k+1个元素起,入堆前和堆顶元素比较，当前元素大，则删除堆顶元素，当前元素入堆
    4.最后堆中保存的就是最大的K个元素
    :param nums:
    :param k:
    :return:
    """
    # 初始化小堆顶
    min_heap = []
    heapq.heapify(min_heap)
    # 前k个元素入堆
    for i in range(k):
        heapq.heappush(min_heap, nums[i])
    # 从k+1个元素起,入堆前和堆顶元素比较，当前元素大，则删除堆顶元素，当前元素入堆
    for i in range(k, len(nums)):
        if nums[i] > min_heap[0]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, nums[i])
    return min_heap


if __name__ == '__main__':
    lst = [7, 4, 3, 6, 5, 2, 1]
    res = get_top_k(lst, k=3)
    print(res)
