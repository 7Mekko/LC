class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []:
            return []
        m = len(matrix)
        n = len(matrix[0])
        cnt = 1
        u , d, l , r = 0 , m-1 , 0 , n-1
        ans = []
        i , j = 0 , 0
        ans.append(matrix[i][j])
        while cnt < m*n and u <= d and l <= r:
            while j+1 <= r:
                j += 1
                ans.append(matrix[i][j])
                cnt += 1
            while i+1 <= d:
                i += 1
                ans.append(matrix[i][j])
                cnt += 1
            if cnt == m*n:
                break
            while j-1 >= l:
                j -= 1
                ans.append(matrix[i][j])
                cnt += 1
            while i-1 >= u+1:
                i -= 1
                ans.append(matrix[i][j])
                cnt += 1
            u , d , l , r = u+1 , d-1 , l+1 , r-1
        return ans