'''下降路径最小和'''
from typing import List


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        d = [[10 ** 9 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            d[0][i] = grid[0][i]
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if j == k:
                        continue
                    d[i][j] = min(d[i][j], d[i - 1][k] + grid[i][j])
        print(d)
        return min(d[n - 1])


if __name__ == '__main__':
    grid = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            ]
    res = Solution().minFallingPathSum(grid)
    print(res)
