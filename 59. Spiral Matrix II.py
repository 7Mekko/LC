class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0 for _ in range(n)]for _ in range(n)]
        cnt = 1
        u , d, l , r = 0 , n-1 , 0 , n-1
        i , j = 0 , 0
        res[i][j] = cnt
        while cnt < n*n and u <= d and l <= r:
            while j+1 <= r:
                j += 1
                cnt += 1
                res[i][j] = cnt
            while i+1 <= d:
                i += 1
                cnt += 1
                res[i][j] = cnt
            if cnt == n*n:
                break
            while j-1 >= l:
                j -= 1
                cnt += 1
                res[i][j] = cnt
            while i-1 >= u+1:
                i -= 1
                cnt += 1
                res[i][j] = cnt
            u , d , l , r = u+1 , d-1 , l+1 , r-1
        return res