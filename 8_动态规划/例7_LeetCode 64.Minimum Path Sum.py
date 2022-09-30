class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]: return 0
        m, n = len(grid), len(grid[0])
        path = copy.deepcopy(grid)
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    before = 0
                elif i == 0:
                    before = path[i][j-1]
                elif j == 0:
                    before = path[i-1][j]
                else:
                    before = min(path[i-1][j], path[i][j-1])
                path[i][j] = before + grid[i][j]
        return path[m-1][n-1]

# https://blog.csdn.net/fuxuemingzhu/article/details/82620422