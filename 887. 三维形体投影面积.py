class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        sum = 0
        g_len = len(grid)
        for i in range(g_len):
            for j in range(len(grid[i])):
                if grid[i][j]!=0:
                    sum += 1
        #print(sum)
        for i in range(g_len):
            max_ = 0
            for j in range(len(grid[i])):
                if grid[i][j]>max_:
                    max_ = grid[i][j]
            sum += max_
        #print(sum)
        for j in range(len(grid[0])):
            max_ = 0
            for i in range(g_len):
                if grid[i][j]>max_:
                    max_ = grid[i][j]
            sum += max_
        return sum


    def __init__(self,grid):
        self.grid = grid
    def getAns(self,grid):
        print(Solution.projectionArea(self,grid))
def main():
    grid = [[1,0],[0,2]]
    S = Solution(grid)
    S.getAns(grid)
if __name__ == '__main__':
    main()