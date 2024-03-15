'''矩阵对角线元素的和'''
from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        res = 0
        for i in range(n):
            res += mat[i][i]
        t = n - 1
        for i in range(n):
            res += mat[t][i]
            t -= 1
        # 判断n是奇数还是偶数
        if n % 2 == 1:
            return res - mat[n // 2][n // 2]
        return res


if __name__ == '__main__':
    mat = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
    res = Solution().diagonalSum(mat)
    print(res)
