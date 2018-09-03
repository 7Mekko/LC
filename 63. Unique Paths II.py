class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        import math
        m = len(obstacleGrid)
        if m == 0 or obstacleGrid[0][0] == 1:
            return 0
        n = len(obstacleGrid[0])
        res = [[1 for _ in range(n)]for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    res[i][j] = 0
                elif i == 0:
                    res[i][j] = res[i][j-1]
                elif j == 0:
                    res[i][j] = res[i-1][j]
                else:
                    res[i][j] = res[i-1][j] + res[i][j-1]
        print(res)
        return res[m-1][n-1]