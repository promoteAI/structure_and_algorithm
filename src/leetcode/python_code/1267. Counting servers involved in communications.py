'''1267. 统计参与通信的服务器
思路：grid[i][j]
判断 grid[i+1][j],grid[i][j+1],grid[i-1][j],grid[i][j-1]是否等于1,为True则该服务器能与其他服务器通信+1，反之将grid[i][j]置为0，
'''
from collections import Counter
from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        n = len(grid)  # 行数
        m = len(grid[0])  # 列数
        rows, cols = Counter(), Counter()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    rows[i] += 1
                    cols[j] += 1
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and (rows[i] > 1 or cols[j] > 1):
                    ans += 1
        return ans


if __name__ == '__main__':
    grid = [[1, 0], [1, 1]]
    # grid = [[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    # grid = [[1, 0, 0, 1, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0]]  # 3
    res = Solution().countServers(grid)
    print(res)
