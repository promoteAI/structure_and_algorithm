from typing import List
import itertools as it
it.permutations()
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new = [i ** 2 for i in nums]
        new.sort()
        return new


res = Solution().sortedSquares(nums=[-7, 0, -9])
print(res)
