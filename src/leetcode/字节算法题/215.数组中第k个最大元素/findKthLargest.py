"""
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。

请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。

 

示例 1:

输入: [3,2,1,5,6,4], k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6], k = 4
输出: 4

"""

from typing import List




# 方法1：先排序，后面直接返回num[-k]
def findKthLargest(nums:List[int],k:int)->int:
    # 返回数组排序后的第k个大的元素
    if len(nums)==1:
        return nums[-k]
    nums=fastSort(nums=nums,l=0,r=len(nums)-1)
    return nums[-k]


def fastSort(nums:List[int],l:int,r:int):
    if l>=r:
        return 
    # 找到哨兵
    pivot = partition(nums,l,r)
    # 递归左子数组
    fastSort(nums,l=l,r=pivot-1)
    # 递归右子数组
    fastSort(nums,l=pivot+1,r=r)
    return nums



def partition(nums:List[int],l:int,r:int):
    i=l
    j=r
    while i<j:
        while i<j and nums[j]>=nums[l]:
            j-=1
        while i<j and nums[i]<=nums[l]:
            i+=1
        # 交换
        nums[i],nums[j]=nums[j],nums[i]
    # 交换基准到中间
    nums[i],nums[l]=nums[l],nums[i]
    return i

# 方法2：使用最小堆（优先队列）- 时间复杂度O(n log k)
def findKthLargest_heap(nums: List[int], k: int) -> int:
    """
    使用最小堆解决第k个最大元素问题
    思路：维护一个大小为k的最小堆，堆顶就是第k个最大元素
    """
    import heapq
    heap = []
    
    for num in nums:
        if len(heap) < k:
            heapq.heappush(heap, num)
        elif num > heap[0]:  # 如果当前元素比堆顶大
            heapq.heapreplace(heap, num)  # 替换堆顶元素
    
    return heap[0]  # 返回堆顶元素（第k个最大元素）


# 方法3：使用最大堆 - 时间复杂度O(n log n)
def findKthLargest_maxheap(nums: List[int], k: int) -> int:
    """
    使用最大堆解决第k个最大元素问题
    思路：将所有元素加入最大堆，然后弹出k-1次，最后堆顶就是第k个最大元素
    """
    import heapq
    # Python的heapq是最小堆，所以用负数模拟最大堆
    max_heap = [-x for x in nums]
    heapq.heapify(max_heap)
    # 弹出k-1个最大元素
    for _ in range(k - 1):
        heapq.heappop(max_heap)
    
    # 返回第k个最大元素
    return -max_heap[0]


# 测试代码
if __name__ == "__main__":
    # 测试用例1
    nums1 = [3, 2, 1, 5, 6, 4]
    k1 = 2
    print(f"测试用例1: nums={nums1}, k={k1}")
    print(f"快速排序方法: {findKthLargest(nums1.copy(), k1)}")
    print(f"最小堆方法: {findKthLargest_heap(nums1.copy(), k1)}")
    print(f"最大堆方法: {findKthLargest_maxheap(nums1.copy(), k1)}")
    
    # 测试用例2
    nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k2 = 4
    print(f"\n测试用例2: nums={nums2}, k={k2}")
    print(f"快速排序方法: {findKthLargest(nums2.copy(), k2)}")
    print(f"最小堆方法: {findKthLargest_heap(nums2.copy(), k2)}")
    print(f"最大堆方法: {findKthLargest_maxheap(nums2.copy(), k2)}")