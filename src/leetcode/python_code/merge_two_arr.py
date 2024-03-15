from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        a = 0
        b = 0
        new = []
        while a < m or b < n:
            if a == m:
                new.append(nums2[b])
                b += 1
            elif b == n:
                new.append(nums1[a])
                a += 1
            elif nums1[a] < nums2[b]:
                new.append(nums1[a])
                a += 1
            else:
                new.append(nums2[b])
                b += 1
        nums1[:] = new
        return nums1


if __name__ == '__main__':
    nums1 = [4, 0, 0, 0, 0, 0]
    m = 1
    nums2 = [1, 2, 3, 5, 6]
    n = 5
    res = Solution().merge(nums1=nums1, m=m, nums2=nums2, n=n)
    print(res)
