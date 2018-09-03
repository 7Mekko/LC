class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == []:
            return False
        m = len(matrix)
        n = len(matrix[0])
        t = 0
        if m == 0 or n == 0 or target < matrix[0][0] or target > matrix[m-1][n-1]:
            return False
        for i in range(m-1):
            if target >= matrix[i][0] and target < matrix[i+1][0]:
                t = i
        if target >= matrix[m-1][0] and target <= matrix[m-1][n-1]:
            t = m - 1
        l = 0
        r = n - 1
        while l <= r:
            m = (l + r) // 2
            if matrix[t][m] == target:
                return True
            if matrix[t][m] < target:
                l = m + 1
            else:
                r = m - 1
        return False