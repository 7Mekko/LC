class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if matrix == []:
            return
        m = len(matrix)
        n = len(matrix[0])
        t = 0
        for j in range(n):
            if matrix[0][j] == 0:
                t = 1
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if i == 0:
                        continue
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        print(matrix)
        for i in range(m-1,0,-1):
            if matrix[i][0] == 0:
                for j in range(n):
                    matrix[i][j] = 0
        print(matrix)
        for j in range(n-1,-1,-1):
            if matrix[0][j] == 0:
                for i in range(m):
                    matrix[i][j] = 0
        if t == 1:
            for j in range(n):
                matrix[0][j] = 0